import time

import allure
import pytest
from selenium.common.exceptions import UnexpectedAlertPresentException

import utils
from utils import get_alert
from web.pabg.home_page import Operate_home_page_object, Home_page_object
from web.pabg.login_page import Operate_login_page_object


class Test_suit:
    def teardown_class(self):
        time.sleep(1)
        utils.Get_driver().quit_driver()

    @pytest.mark.run(order=1001)
    @pytest.mark.parametrize("username,password,expect",
                             [(431011210, "3edc$RFV", "用户名不存在！"), (431011211, "123456", "密码不正确！")])
    @allure.step(title="登录失败")
    def test_login_failed(self, username, password, expect):
        Operate_login_page_object().click_login_btn(username, password)
        time.sleep(1)
        # allure.attach(utils.Get_driver().driver.get_screenshot_as_png(), "登录失败弹窗", allure.attachment_type.PNG)
        # 无法在有弹窗的情况下截图
        try:
            ex = get_alert().text
            get_alert().accept()
        except UnexpectedAlertPresentException:
            ex = get_alert().text
            print("执行的是except______", get_alert().text)
            get_alert().accept()
        allure.attach(utils.Get_driver().driver.get_screenshot_as_png(), "登录失败弹窗", allure.attachment_type.PNG)
        time.sleep(1)
        assert expect == ex  # 断言失败后不会执行assert下面的代码

    @pytest.mark.run(order=1002)
    @allure.step(title="登录成功")
    def test_login_success(self):
        Operate_login_page_object().click_login_btn("431011211", "3edc$RFV")
        time.sleep(2)
        allure.attach(utils.Get_driver().get_web_driver().get_screenshot_as_png(), "登录成功进入主页", allure.attachment_type.PNG)
        assert Home_page_object().account_information_element().text == "长沙县公路建设养护中心(农村公路)"

    @pytest.mark.run(order=1003)
    @allure.step(title="删除采集记录成功")
    def test_operation(self):
        Operate_home_page_object().operate_delete_record()
        allure.attach(utils.Get_driver().get_web_driver().get_screenshot_as_png(), "删除采集记录成功", allure.attachment_type.PNG)
        time.sleep(1)
        assert Home_page_object().delete_success
