from selenium.webdriver.common.by import By
import utils
from appv1.pabg.app_collection_page import Operate_choice_page_object


class Login_page_object:
    def __init__(self):
        self.driver = utils.Get_driver.get_app_driver()
        # 查找各元素的值
        self.username = By.ID, "com.vondear.onemap:id/ed_unit_code"
        self.password = By.ID, "com.vondear.onemap:id/ed_password"
        self.collector = By.ID, "com.vondear.onemap:id/ed_collect_name"
        self.collector_telephone = By.ID, "com.vondear.onemap:id/ed_collect_phone"
        self.login_btn = By.ID, "com.vondear.onemap:id/btn_login"


    def username_element(self):
        return utils.get_element(self.driver, self.username)

    def password_element(self):
        return utils.get_element(self.driver, self.password)

    def collector_element(self):
        return utils.get_element(self.driver, self.collector)

    def collector_telephone_element(self):
        return utils.get_element(self.driver, self.collector_telephone)

    def login_btn_element(self):
        return utils.get_element(self.driver, self.login_btn)

    def toast_element(self,expect):
        toast = By.XPATH, "//*[contains(@text, '{}')]".format(expect)
        return utils.get_element(self.driver, toast)


class Operate_login_page_object:
    def __init__(self):
        self.l_p_o = Login_page_object()

    def click_login_btn(self, username, password, collector, collector_telephone):
        utils.send_text(self.l_p_o.username_element(), username)
        utils.send_text(self.l_p_o.password_element(), password)
        utils.send_text(self.l_p_o.collector_element(), collector)
        utils.send_text(self.l_p_o.collector_telephone_element(), collector_telephone)
        self.l_p_o.login_btn_element().click()
