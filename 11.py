# забрать значение из тега, вставить в формулу, чек бокс, радио батон, кнопка
from re import X
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/get_attribute.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = x_element.get_attribute("valuex")
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)
    time.sleep(1)
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()
    button =  browser.find_element(By.CSS_SELECTOR, '.btn').click()
finally: 
    time.sleep(10) 
    browser.quit()