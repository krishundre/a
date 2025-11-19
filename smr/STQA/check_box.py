from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")

checkbox1 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[1]")
checkbox2 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[2]")

checkbox1.click()
time.sleep(5)
checkbox1.click()
time.sleep(5)
checkbox2.click()
time.sleep(5)
checkbox2.click()
time.sleep(5)
if not checkbox1.is_selected():
    checkbox1.click()

    time.sleep(5)
if not checkbox2.is_selected():
    checkbox2.click()
    time.sleep(5)


driver.quit()
