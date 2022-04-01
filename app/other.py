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
            print(cls.driver)
        #print(cls.driver)
        return cls.driver
Apptest.get_driver().find_element(By.ID, "com.vondear.onemap:id/ed_unit_code").send_keys("1111")
Apptest.get_driver().find_element(By.ID,  "com.vondear.onemap:id/ed_password").send_keys("222")
#什么意思啊
