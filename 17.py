# ждем выполнение условий и нажимаем на кнопку, решаем формулу,ок
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time 
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    btn = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))# ждем 15 сек или пока по ID price текст станет 100$
    button = browser.find_element(By.ID, "book").click()
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    button2 =  browser.find_element(By.ID, 'solve').click()
finally: 
    time.sleep(10) 
    browser.quit()