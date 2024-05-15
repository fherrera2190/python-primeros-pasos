import logging
from datetime import datetime
logger = logging.getLogger('certification3')
logger.setLevel(logging.DEBUG)
file_handler=logging.FileHandler('D:/log.log')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.info('Start robot')


file_handler.close()
logger.removeHandler(file_handler)