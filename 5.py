
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
url = 'https://demowebshop.tricentis.com'
try:
    browser.get(url)
    prod_1 = browser.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[3]/div/div/div[3]/div[3]/div/div[2]/h2/a").click()
    sleep(3)
    addToCart = browser.find_element(By.XPATH, '//*[@id="add-to-cart-button-31"]').click()
    sleep(3)
    cart = browser.find_element(By.XPATH, '//*[@id="topcartlink"]/a/span[1]').click()
    sleep(3)

    # goods = browser.find_elements_by_css_selector('.container:nth-child(3) .a7m4')
    # print(goods)
    # print(len(goods))

    # assert len(goods) == 3, 'в корзине не 3 вещи'
finally:
    sleep(5)
    browser.close()
    browser.quit()
    