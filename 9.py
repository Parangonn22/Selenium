#зайти на сайт, посчитать формулу, вставить значение из резцльтата формулы, чек-бок, радио баттон, кнопка
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "https://suninjuly.github.io/math.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)
    time.sleep(1)
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option2.click()
    button =  browser.find_element(By.CSS_SELECTOR, '.btn').click()
finally: 
    time.sleep(10) 
    browser.quit()
