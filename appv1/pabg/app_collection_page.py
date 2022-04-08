import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import utils


def dianjicaiji():
    action = TouchAction(utils.Get_driver.get_app_driver())
    action.tap(x=520, y=1830).perform()
    time.sleep(1)
    action.tap(x=730, y=1790).perform()


def shanghua_caiji():
    action = TouchAction(utils.Get_driver.get_app_driver())
    action.press(x=500, y=1310).move_to(x=500, y=800).release().perform()


def dianjitouxiang():
    action = TouchAction(utils.Get_driver.get_app_driver())
    action.tap(x=105, y=175).perform()
    time.sleep(1)
    action.tap(x=365, y=775).perform()
    time.sleep(1)
    action.press(x=855, y=310).wait(1).move_to(x=270, y=310).release().perform()


class Collection_page_object:
    def __init__(self):
        self.driver = utils.Get_driver.get_app_driver()
        # 查找各元素的值
        self.annual_report_collection = By.ID, "com.vondear.onemap:id/rb0"  # CSS中不能有反斜杠
        self.road_environment_improvement_btn = By.ID, "com.vondear.onemap:id/btn_point_environment"
        self.first_collect = By.CLASS_NAME, "android.widget.LinearLayout"
        self.discovery_time = By.ID, "com.vondear.onemap:id/tv_wffxsj"
        self.discovery_position = By.ID, "com.vondear.onemap:id/tv_wz"
        self.position_select = By.XPATH, "//*[@text='公路用地']"
        self.xz = By.ID, "com.vondear.onemap:id/tv_xz"
        self.xz_select = By.XPATH, "//*[@text='违法设施']"
        self.wfsm = By.ID, "com.vondear.onemap:id/et_wfsm"
        self.pszmzp = By.XPATH, "//*[@text='拍摄正面照片']"
        self.djpz = By.ID, "com.vondear.onemap:id/btn_take_photo1"
        self.djpzqd = By.ID, "com.vondear.onemap:id/tv_sure1"
        self.pscmzp = By.XPATH, "//*[@text='拍摄侧面照片1']"
        self.cjwc_btn = By.ID, "com.vondear.onemap:id/btn_sure"
        self.sc = By.XPATH, "//*[@text='路域环境整治']"
        self.sc_1 = By.ID, "com.vondear.onemap:id/card_view"
        self.sc_2 = By.XPATH, "//*[@text='在线上传']"
        self.sfsccg = By.ID, "com.vondear.onemap:id/tv_content"

    def annual_report_collection_btn_element(self):
        return utils.get_element(self.driver, self.annual_report_collection)

    def road_environment_improvement_btn_element(self):
        return utils.get_element(self.driver, self.road_environment_improvement_btn)

    def first_collect_element(self):
        return utils.get_element(self.driver, self.first_collect)

    def discovery_time_element(self):
        return utils.get_element(self.driver, self.discovery_time)

    def discovery_position_element(self):
        return utils.get_element(self.driver, self.discovery_position)

    def position_select_element(self):
        return utils.get_element(self.driver, self.position_select)

    def xz_element(self):
        return utils.get_element(self.driver, self.xz)

    def xz_select_element(self):
        return utils.get_element(self.driver, self.xz_select)

    def wfsm_element(self):
        return utils.get_element(self.driver, self.wfsm)

    def pszmzp_element(self):
        return utils.get_element(self.driver, self.pszmzp)

    def djpz_element(self):
        return utils.get_element(self.driver, self.djpz)

    def djpzqd_element(self):
        return utils.get_element(self.driver, self.djpzqd)

    def pscmzp_element(self):
        return utils.get_element(self.driver, self.pscmzp)

    def cjwc_btn_element(self):
        return utils.get_element(self.driver, self.cjwc_btn)

    def sc_element(self):
        return utils.get_element(self.driver, self.sc)

    def sc_1_element(self):
        return utils.get_element(self.driver, self.sc_1)

    def sc_2_element(self):
        return utils.get_element(self.driver, self.sc_2)

    def sfsccg_element(self):
        return utils.get_element(self.driver, self.sfsccg)


class Operate_choice_page_object:
    def __init__(self):
        self.l_p_o = Collection_page_object()

    def collection_successful(self):
        time.sleep(3)
        self.l_p_o.annual_report_collection_btn_element().click()
        time.sleep(8)
        dianjicaiji()
        self.l_p_o.road_environment_improvement_btn_element().click()
        time.sleep(8)
        self.l_p_o.first_collect_element().click()
        self.l_p_o.discovery_time_element().send_keys("2022-3-9")
        self.l_p_o.discovery_position_element().click()
        self.l_p_o.position_select_element().click()
        self.l_p_o.xz_element().click()
        self.l_p_o.xz_select_element().click()
        self.l_p_o.wfsm_element().send_keys("test")
        self.l_p_o.pszmzp_element().click()
        self.l_p_o.djpz_element().click()
        time.sleep(8)
        self.l_p_o.djpzqd_element().click()
        time.sleep(8)
        self.l_p_o.pscmzp_element().click()
        # 侧面拍照
        self.l_p_o.djpz_element().click()
        time.sleep(8)
        self.l_p_o.djpzqd_element().click()
        time.sleep(8)
        # shanghua_caiji()
        self.l_p_o.cjwc_btn_element().click()

    def upload_collection_record(self):
        time.sleep(3)
        dianjitouxiang()
        self.l_p_o.sc_element().click()
        self.l_p_o.sc_1_element().click()
        self.l_p_o.sc_2_element().click()
