import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    firstname = browser.find_element(By.XPATH, "//input[@placeholder='Enter first name']")
    firstname.send_keys("My_firstname")

    lastname = browser.find_element(By.XPATH, "//input[@placeholder='Enter last name']")
    lastname.send_keys("My_last_name")

    email = browser.find_element(By.XPATH, "//input[@placeholder='Enter email']")
    email.send_keys("My_email")

    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()