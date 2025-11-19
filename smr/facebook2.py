import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
time.sleep(2)

# explicit wait
wait = WebDriverWait(driver, 10)

# get current window handle
original_window = driver.current_window_handle
print(original_window, type(original_window))  # this prints the handle (a string)

# open a new empty window
driver.switch_to.new_window('window')

# wait until the number of windows becomes 2
wait.until(EC.number_of_windows_to_be(2))
time.sleep(2)

# open Google in a new tab
driver.execute_script("window.open('http://www.google.com/');")

# wait until the number of windows becomes 3
wait.until(EC.number_of_windows_to_be(3))

# get all window handles
all_windows = driver.window_handles
print(all_windows, type(all_windows))  # prints list of window handles

# switch to any window that is not the original one
for window in all_windows:
    if window != original_window:
        driver.switch_to.window(window)
        break