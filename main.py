from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://demoqa.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Ele')]//../..").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Alert')]//../..").click()
time.sleep(3)
driver.find_element(by=By.CSS_SELECTOR, value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(10)
driver.find_element(by=By.XPATH, value="//span[contains(text(), 'Browser')]").click()
time.sleep(5)
driver.find_element(by=By.XPATH, value="//button[@id = 'tabButton']").click()
current_window = driver.current_window_handle
all_windows = driver.window_handles
for next_window in all_windows:
    if next_window != current_window:
        driver.switch_to.window(next_window)
text = driver.find_element(by=By.XPATH, value= "//h1[@id = 'sampleHeading']").text
print(text)
if text == "This is a sample page":
    print("success")

time.sleep(10)
