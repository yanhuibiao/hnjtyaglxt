import time

from selenium.webdriver.common.by import By
import utils


class Login_page_object:
    def __init__(self):
        self.driver = utils.Get_driver.get_web_driver()
        self.username = By.XPATH, "//*[@class='login__input name']"
        self.password = By.XPATH, "//*[@class='login__input pass']"
        self.login_btn = By.CSS_SELECTOR, "#loginBtn"

    def username_element(self):
        return utils.get_element(self.driver, self.username)

    def password_element(self):
        return utils.get_element(self.driver, self.password)

    def login_btn_element(self):
        return utils.get_element(self.driver, self.login_btn)


class Operate_login_page_object:
    def __init__(self):
        self.l_p_o = Login_page_object()

    def click_login_btn(self, username, password):
        utils.send_text(self.l_p_o.username_element(), username)
        utils.send_text(self.l_p_o.password_element(), password)
        self.l_p_o.login_btn_element().click()
