import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver_path = "/Users/sebastianbarona/Downloads/pyton/chromedriver"

driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get("https://conexiones.saviasaludeps.com/savia/")


elem = driver.find_element_by_id("login:usuario")
elem.send_keys("900421895r01")

elem = driver.find_element_by_id("login:contrasena")
elem.send_keys("Fundacion2021*")

time.sleep(2)
elem = driver.find_element_by_id("login:j_idt24")
elem.click()


driver.get("https://conexiones.saviasaludeps.com/savia/cuenta_medica/rips/carga_rips.faces")
time.sleep(1)
elem = driver.find_element_by_id("frmRipsCargas:j_idt46")
elem.click()

#NUMERO DE ENVIO
elem = driver.find_element_by_id("frmCrear:j_idt145_input")
elem.send_keys("12345")

#FECHA PRESTACION  - FECHA EN QUE SE CERRO LA FACTURA
elem = driver.find_element_by_id("frmCrear:mesPrestacion_input")
elem.send_keys("2021-02")

#VALOR BRUTO
elem = driver.find_element_by_id("frmCrear:valorCuenta_input")
elem.send_keys("120000")

#CONTRATO
elem = driver.find_element_by_id("frmCrear:contrato")
elem.send_keys("0001-2021")

