# нажать кнопку, перейти в новое окно, выполнить формулу, ок
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    btn1 = browser.find_element(By.CSS_SELECTOR, ".trollface").click()
    new_window = browser.window_handles[1]#называем новое окно
    browser.switch_to.window(new_window)#переключаемся на него
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)
    button =  browser.find_element(By.CSS_SELECTOR, '.btn').click()
finally: 
    time.sleep(10) 
    browser.quit()