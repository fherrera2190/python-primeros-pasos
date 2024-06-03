"""
Module for managing the download of Selenium webdriver binaries.

This code is released under the MIT license.
"""
import abc
import logging
import os
import os.path
from pathlib import Path
import platform
import shutil
import stat
import tarfile
try:
    from urlparse import urlparse, urlsplit  # Python 2.x import
except ImportError:
    from urllib.parse import urlparse, urlsplit  # Python 3.x import
import zipfile

from bs4 import BeautifulSoup
import requests
import tqdm

from .util import get_architecture_bitness


logger = logging.getLogger(__name__)


class WebDriverDownloaderBase:
    """Abstract Base Class for the different web driver downloaders
    """

    __metaclass__ = abc.ABCMeta

    def __init__(self, download_root=None, link_path=None, os_name=None):
        """
        Initializer for the class.  Accepts three optional parameters.

        :param download_root: Path where the web driver binaries will be downloaded.  If running as root in macOS or
                              Linux, the default will be '/usr/local/webdriver', otherwise will be '$HOME/webdriver'.
        :param link_path: Path where the link to the web driver binaries will be created.  If running as root in macOS
                          or Linux, the default will be 'usr/local/bin', otherwise will be '$HOME/bin'.  On macOS and
                          Linux, a symlink will be created.
        :param os_name: Name of the OS to download the web driver binary for, as a str.  If not specified, we will use
                        platform.system() to get the OS.
        """
        if os_name is None:
            os_name = platform.system()
        if os_name in ['Darwin', 'Linux'] and os.geteuid() == 0:
            base_path = "/usr/local"
        else:
            base_path = os.path.expanduser("~")

        if download_root is None:
            self.download_root = os.path.join(base_path, "webdriver")
        else:
            self.download_root = download_root

        if link_path is None:
            self.link_path = os.path.join(base_path, "bin")
        else:
            self.link_path = link_path

        if not os.path.isdir(self.download_root):
            os.makedirs(self.download_root)
            logger.info("Created download root directory: {0}".format(self.download_root))
        if not os.path.isdir(self.link_path):
            os.makedirs(self.link_path)
            logger.info("Created symlink directory: {0}".format(self.link_path))

    @abc.abstractmethod
    def get_driver_filename(self, os_name=None):
        """
        Method for getting the filename of the web driver binary.

        :param os_name: Name of the OS to download the web driver binary for, as a str.  If not specified, we will use
                        platform.system() to get the OS.
        :returns: The filename of the web driver binary.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_download_path(self, version="latest"):
        """
        Method for getting the target download path for a web driver binary.

        :param version: String representing the version of the web driver binary to download.  For example, "2.38".
                        Default if no version is specified is "latest".  The version string should match the version
                        as specified on the download page of the webdriver binary.

        :returns: The target download path of the web driver binary.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_download_url(self, version="latest", os_name=None, bitness=None):
        """
        Method for getting the source download URL for a web driver binary.

        :param version: String representing the version of the web driver binary to download.  For example, "2.38".
                        Default if no version is specified is "latest".  The version string should match the version
                        as specified on the download page of the webdriver binary.
        :param os_name: Name of the OS to download the web driver binary for, as a str.  If not specified, we will use
                        platform.system() to get the OS.
        :param bitness: Bitness of the web driver binary to download, as a str e.g. "32", "64".  If not specified, we
                        will try to guess the bitness by using util.get_architecture_bitness().
        :returns: The source download URL for the web driver binary.
        """
        raise NotImplementedError

    def download(self, version="latest", os_name=None, bitness=None, show_progress_bar=True):
        """
        Method for downloading a web driver binary.

        :param version: String representing the version of the web driver binary to download.  For example, "2.38".
                        Default if no version is specified is "latest".  The version string should match the version
                        as specified on the download page of the webdriver binary.  Prior to downloading, the method
                        will check the local filesystem to see if the driver has been downloaded already and will
                        skip downloading if the file is already present locally.
        :param os_name: Name of the OS to download the web driver binary for, as a str.  If not specified, we will use
                        platform.system() to get the OS.
        :param bitness: Bitness of the web driver binary to download, as a str e.g. "32", "64".  If not specified, we
                        will try to guess the bitness by using util.get_architecture_bitness().
        :param show_progress_bar: Boolean (default=True) indicating if a progress bar should be shown in the console.
        :returns: The path + filename to the downloaded web driver binary.
        """
        download_url = self.get_download_url(version, os_name=os_name, bitness=bitness)
        filename = os.path.split(urlparse(download_url).path)[1]
        filename_with_path = os.path.join(self.get_download_path(version), filename)
        if not os.path.isdir(self.get_download_path(version)):
            os.makedirs(self.get_download_path(version))
        if os.path.isfile(filename_with_path):
            logger.info("Skipping download. File {0} already on filesystem.".format(filename_with_path))
            return filename_with_path
        data = requests.get(download_url, stream=True)
        if data.status_code == 200:
            logger.debug("Starting download of {0} to {1}".format(download_url, filename_with_path))
            with open(filename_with_path, mode="wb") as fileobj:
                chunk_size = 1024
                if show_progress_bar:
                    expected_size = int(data.headers['Content-Length'])
                    for chunk in tqdm.tqdm(data.iter_content(chunk_size),
                                           total=int(expected_size / chunk_size),
                                           unit='kb'):
                        fileobj.write(chunk)
                else:
                    for chunk in data.iter_content(chunk_size):
                        fileobj.write(chunk)
            logger.debug("Finished downloading {0} to {1}".format(download_url, filename_with_path))
            return filename_with_path
        else:
            error_message = "Error downloading file {0}, got status code: {1}".format(filename, data.status_code)
            logger.error(error_message)
            raise RuntimeError(error_message)

    def download_and_install(self, version="latest", os_name=None, bitness=None, show_progress_bar=True, extract_path=''):
        """
        Method for downloading a web driver binary, extracting it into the download directory and creating a symlink
        to the binary in the link directory.

        :param version: String representing the version of the web driver binary to download.  For example, "2.38".
                        Default if no version is specified is "latest".  The version string should match the version
                        as specified on the download page of the webdriver binary.
        :param os_name: Name of the OS to download the web driver binary for, as a str.  If not specified, we will use
                        platform.system() to get the OS.
        :param bitness: Bitness of the web driver binary to download, as a str e.g. "32", "64".  If not specified, we
                        will try to guess the bitness by using util.get_architecture_bitness().
        :param show_progress_bar: Boolean (default=True) indicating if a progress bar should be shown in the console.
        :returns: Tuple containing the path + filename to [0] the extracted binary, and [1] the symlink to the
                  extracted binary.
        """
        filename_with_path = self.download(version,
                                           os_name=os_name,
                                           bitness=bitness,
                                           show_progress_bar=show_progress_bar)
        filename = os.path.split(filename_with_path)[1]
        if filename.lower().endswith(".tar.gz"):
            extract_dir = os.path.join(self.get_download_path(version), filename[:-7])
        elif filename.lower().endswith(".zip"):
            extract_dir = os.path.join(self.get_download_path(version), filename[:-4])
        else:
            error_message = "Unknown archive format: {0}".format(filename)
            logger.error(error_message)
            raise RuntimeError(error_message)
        if not os.path.isdir(extract_dir):
            os.makedirs(extract_dir)
            logger.debug("Created directory: {0}".format(extract_dir))
        if filename.lower().endswith(".tar.gz"):
            with tarfile.open(os.path.join(self.get_download_path(version), filename), mode="r:*") as tar:
                tar.extractall(extract_dir)
                logger.debug("Extracted files: {0}".format(", ".join(tar.getnames())))
        elif filename.lower().endswith(".zip"):
            with zipfile.ZipFile(os.path.join(self.get_download_path(version), filename), mode="r") as driver_zipfile:
                driver_zipfile.extractall(extract_path)
                #driver_zipfile.extractall(extract_dir)
        driver_filename = self.get_driver_filename(os_name=os_name)
        for root, dirs, files in os.walk(extract_path):
            for curr_file in files:
                if curr_file == driver_filename:
                    actual_driver_filename = os.path.join(root, curr_file)
                    break
        if os_name is None:
            os_name = platform.system()
        if os_name in ['Darwin', 'Linux']:
            symlink_src = actual_driver_filename
            symlink_target = os.path.join(self.link_path, driver_filename)
            if os.path.islink(symlink_target):
                if os.path.samefile(symlink_src, symlink_target):
                    logger.info("Symlink already exists: {0} -> {1}".format(symlink_target, symlink_src))
                    return tuple([symlink_src, symlink_target])
                else:
                    logger.warning("Symlink {0} already exists and will be overwritten.".format(symlink_target))
                    os.unlink(symlink_target)
            os.symlink(symlink_src, symlink_target)
            logger.info("Created symlink: {0} -> {1}".format(symlink_target, symlink_src))
            st = os.stat(symlink_src)
            os.chmod(symlink_src, st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
            return tuple([symlink_src, symlink_target])
        elif os_name == "Windows":
            src_file = actual_driver_filename
            dest_file = os.path.join(self.link_path, driver_filename)
            if os.path.isfile(dest_file):
                logger.info("File {0} already exists and will be overwritten.".format(dest_file))
            shutil.copy2(src_file, dest_file)
            return tuple([src_file, dest_file])