import time

import allure
import pytest

import utils
from appv1.pabg.app_collection_page import Operate_choice_page_object
from appv1.pabg.app_login_page import Operate_login_page_object, Login_page_object


class Test_suit:
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("username,password,collector,collector_telephone,expect", utils.get_app_data())
    @allure.step(title="登录测试")
    def test_login(self, username, password, collector, collector_telephone, expect):
        Operate_login_page_object().click_login_btn(username, password, collector, collector_telephone)
        # time.sleep(0.5)
        a = Login_page_object().toast_element(expect)
        allure.attach(utils.Get_driver().driver.get_screenshot_as_png(), "登录信息弹窗", allure.attachment_type.PNG)
        assert a

    @pytest.mark.run(order=2)
    @allure.step(title="采集步骤测试")
    def test_cj(self):
        Operate_choice_page_object().collection_successful()
        a = Login_page_object().toast_element("采集成功")
        allure.attach(utils.Get_driver().driver.get_screenshot_as_png(), "采集信息弹窗", allure.attachment_type.PNG)
        assert a

    @pytest.mark.run(order=3)
    @allure.step(title="上传采集记录测试")
    def test_upload(self):
        Operate_choice_page_object().upload_collection_record()
        a = Login_page_object().toast_element("上传成功")
        allure.attach(utils.Get_driver().driver.get_screenshot_as_png(), "上传信息弹窗", allure.attachment_type.PNG)
        assert a