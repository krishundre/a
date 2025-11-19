#from selenium import webdriver

# webdriver.Chrome().get('https://www.google.com')

#10-09-2025
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://google.com")
# driver.refresh()
# driver.forward()
# driver.back()

# Print current URL, title, and page source
print("Current URL:", driver.current_url)
print("Page Title:", driver.title)
print("Page Source Length:", len(driver.page_source))  # Just showing length, not full HTML

#search_textbox=driver.find_element(By.XPATH,"//textarea[@name='q']")

#single_search_textbox= driver.find_element(By.XPATH,"//textarea ")

#multi_search_textbox= driver.find_elements(By.XPATH,"//textarea ")

# print(type(single_search_textbox))
# print(type(multi_search_textbox))

# print(single_search_textbox)
# print(multi_search_textbox)

#multi_search_textbox.send_keys('imcc')
#multi_search_textbox.send_keys(Keys.ENTER)



#search_textbox.send_keys("imcc")
#search_textbox.send_keys(Keys.ENTER)
# driver.send_keys(Keys.ENTER)
#
# search_textbox.clear()
# search_textbox.send_keys(Keys.ENTER)
#

# title=driver.title
# print(title)
#
# current_url=driver.current_url
# print(current_url)
#
# source=driver.page_source
# print(source)
#
# driver.fullscreen_window()
# driver.maximize_window()
# driver.refresh()