from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import utils
from selenium.common.exceptions import UnexpectedAlertPresentException

driver = webdriver.Edge()
driver.get("http://10.200.255.6:8090/login")

username = By.XPATH, "//*[@class='login__input name']"
password = By.XPATH, "//*[@class='login__input pass']"
login_btn = By.CSS_SELECTOR, "#loginBtn"

def username_element():
    return utils.get_element(driver, username)

def password_element():
    return utils.get_element(driver, password)

def login_btn_element():
    return utils.get_element(driver, login_btn)



utils.send_text(username_element(), "431011210")
utils.send_text(password_element(), "123456")
login_btn_element().click()
time.sleep(3)
try:
    print(driver.switch_to.alert.text)
except UnexpectedAlertPresentException:
    print(driver.switch_to.alert.text)
    driver.switch_to.alert.accept()
    # driver.delete_all_cookies()
    time.sleep(3)


