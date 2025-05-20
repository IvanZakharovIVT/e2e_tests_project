from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    firstname.send_keys("My_firstname")

    lastname = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    lastname.send_keys("My_last_name")

    email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    email.send_keys("My_email")

    phone = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
    phone.send_keys("My_phone")

    address = browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']")
    address.send_keys("My_address")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
