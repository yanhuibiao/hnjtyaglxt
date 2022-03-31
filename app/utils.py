from appium import webdriver
from selenium.webdriver.common.by import By
import pytest

config = {"platformName": "android",  # 表示的是android  或者ios
          "platformVersion": "7.1.2",  # 表示的是平台系统的版本号
          "deviceName": "emulator-5554",  # 表示的是设备的ID名称（如果只有一个设备可以用****来代替）
          "appPackage": "com.vondear.onemap",  # 表示app的包名
          "appActivity": ".activity.ActivityLogin",  # 表示的是app的界面名
          "noReset": True,  # 用来记住app的session，如果有登陆或做过初始化的操作，为True时，后面不需要再操作
          "resetKeyboard": True,  # 重置设备的输入键盘
          "unicodeKeyboard": True,  # 键盘编码
          "automationName": "Uiautomator2"}  # 获取toast消息
command_executor = "http://127.0.0.1:4723/wd/hub"


class Apptest:
    driver = None
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Remote(command_executor, config)
        return cls.driver
    @classmethod
    def quit_driver(cls):
        cls.driver.quit()
        cls.driver = None

    @classmethod
    def element(cls,By,find_values,clear=None,send_keys=None,send_keys_values=None,click=None):
        ele =cls.get_driver().find_element(By,find_values)
        if clear == 1:
            ele.clear()
        if send_keys == 1:
            ele.send_keys(send_keys_values)
        if click == 1:
            ele.click()
        return ele









