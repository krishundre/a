from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com")
search_box =driver.find_element(By.NAME, "q")

print("autocomplete:",search_box.get_attribute("autocomplete"))
print("id",search_box.get_attribute("id"))

print("value(before typing):",search_box.get_attribute("value"))
search_box.send_keys("IMCC")
print("value(after typing):",search_box.get_attribute("value"))

driver.quit()