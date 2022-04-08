import time

from selenium.webdriver.common.by import By
import utils


class Home_page_object:
    def __init__(self):
        self.driver = utils.Get_driver.get_web_driver()
        self.account_information = By.CSS_SELECTOR, ".hidden-xs"
        self.data_update = By.XPATH, "//*[text() = '数据更新']"
        self.road_regulation_management = By.XPATH, "// *[text() = '路域整治管理']"
        self.delete_record = By.XPATH, "//*[@class='DTFC_RightWrapper']/div[2]/div[1]/table/tbody/tr/td/a[4]"
        self.sure_delete =By.XPATH, "//*[@class='btn btn-primary btn-smModal']"

    def account_information_element(self):
        return utils.get_element(self.driver, self.account_information)

    def data_update_element(self):
        return utils.get_element(self.driver, self.data_update)

    def road_regulation_management_element(self):
        return utils.get_element(self.driver, self.road_regulation_management)

    def delete_record_element(self):
        return utils.get_element(self.driver, self.delete_record)

    def sure_delete_element(self):
        return utils.get_element(self.driver, self.sure_delete)

    def delete_success(self):
        return utils.get_element(self.driver, (By.XPATH, "//*[text()='删除成功']"))


class Operate_home_page_object:
    def __init__(self):
        self.h_p_o = Home_page_object()

    def operate_delete_record(self):
        self.h_p_o.data_update_element().click()
        self.h_p_o.road_regulation_management_element().click()
        time.sleep(5)
        self.h_p_o.delete_record_element().click()
        self.h_p_o.sure_delete_element().click()






