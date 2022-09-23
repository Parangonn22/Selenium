from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    browser.execute_script("window.scrollBy(0, 100);")
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
    button =  browser.find_element(By.CSS_SELECTOR, '.btn').click()
finally: 
    time.sleep(10) 
    browser.quit()
