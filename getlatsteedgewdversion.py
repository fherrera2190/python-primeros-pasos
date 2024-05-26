import requests

url = 'https://msedgedriver.azureedge.net/LATEST_STABLE'
response = requests.get(url)

if response.status_code == 200:
    latest_version = response.text.strip()
    print(f"La última versión estable de Edge WebDriver es: {latest_version}")
    print(latest_version)
else:
    print("No se pudo obtener la última versión de Edge WebDriver")
