from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
# Ruta al GeckoDriver
driver_path = '/home/kali/Downloads/geckodriver'

# Configura el servicio de GeckoDriver
service = Service(executable_path=driver_path)

# Configura las opciones de Firefox
options = Options()
options.set_preference("dom.webdriver.enabled", False)
options.set_preference("useAutomationExtension", False)
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Inicializa el WebDriver de Firefox usando el servicio y las opciones
driver = webdriver.Firefox(service=service, options=options)

try:
    # Abre la página web
    driver.get('https://www.livejasmin.com/es/girls')
    time.sleep(50)

finally:
    # Cierra el navegador
    driver.quit()
