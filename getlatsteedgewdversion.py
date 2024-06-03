import requests
import sys
import os
import platform
url = 'https://msedgedriver.azureedge.net/LATEST_STABLE'
response = requests.get(url)

if response.status_code == 200:
    latest_version = response.text.strip()
    response = url+"/"+latest_version+"/"+"msedgedriver.exe"
    print(response)
    print(f"La última versión estable de Edge WebDriver es: {latest_version}")
    print(latest_version)
else:
    print("No se pudo obtener la última versión de Edge WebDriver")

print("----------------------------")

# print(os.getcwd())
# print(os.path.realpath(__file__))
# print(os.path.dirname(os.path.realpath(__file__)))

print(os.path.expanduser("~"))

new_directory = os.path.join(os.path.expanduser("~"), "mi_nuevo_directorio")

# Verificar si el directorio ya existe
# if not os.path.exists(new_directory):
#     os.makedirs(new_directory)

print(platform.system())