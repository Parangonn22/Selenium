# взяли значение а и в, посчитали сумму, выбрали из списка нужный ответ
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    aTeg = browser.find_element(By.CSS_SELECTOR, '#num1')
    bTeg = browser.find_element(By.CSS_SELECTOR, '#num2')
    a = int(aTeg.text)
    b = int(bTeg.text)
    c = str(a+b)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(c)
    button =  browser.find_element(By.CSS_SELECTOR, '.btn').click()
finally: 
    time.sleep(10) 
    browser.quit()