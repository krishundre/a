from concurrent.futures import thread

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.google.com/")
driver.refresh()
driver.get("www.youtube.com")
driver.refresh()
driver.backward()
driver.forward()
#print(driver.page_source)

#driver.maximize_window()
#driver.quit()
#search_txtbox = driver.find_element(By.XPATH,"//textarea[@name='q']")
#search_txtbox.send_keys("IMCC")


#driver.get()
#driver.send_keys(Keys.ENTER)
print("Press enter to continue...")