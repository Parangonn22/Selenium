from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
link = "http://suninjuly.github.io/registration1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.XPATH,"/html/body/div/form/div[1]/div[1]/input")
    input1.send_keys("Denis")
    input2 = browser.find_element(By.XPATH,"/html/body/div/form/div[1]/div[2]/input")
    input2.send_keys("Shevchenko")
    input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
    input3.send_keys("mail@gmail.com")
    input4 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[1]/input")
    input4.send_keys("066121212")
    input5 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[2]/input")
    input5.send_keys("Ukraine")
    time.sleep(3)
    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()
    time.sleep(4)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally: 
    time.sleep(10) 
    browser.quit()