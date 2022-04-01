from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

desired_capabilities = {"platformName": "android",  # 表示的是android  或者ios
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
            cls.driver = webdriver.Remote(command_executor, desired_capabilities)
            cls.driver.implicitly_wait(3)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        cls.driver.quit()
        cls.driver = None

    @classmethod
    def element(cls, by, find_values, clear=None, send_keys=None, send_keys_values=None, click=None):
        if by == 'By.ID':
            by = By.ID
        elif by == "By.XPATH":
            by = By.XPATH
        elif by == "By.LINK_TEXT":
            by = By.LINK_TEXT
        elif by == "By.PARTIAL_LINK_TEXT":
            by = By.PARTIAL_LINK_TEXT
        elif by == "By.NAME":
            by = By.NAME
        elif by == "By.TAG_NAME":
            by = By.TAG_NAME
        elif by == "By.CLASS_NAME":
            by = By.CLASS_NAME
        elif by == "By.CSS_SELECTOR":
            by = By.CSS_SELECTOR
        else:
            raise Exception("请输入正确的by")
        ele = WebDriverWait(Apptest.get_driver(), 5, 0.5).until(lambda x: x.find_element(by, find_values))
        if clear == 1:
            ele.clear()
        if send_keys == 1:
            ele.send_keys(send_keys_values)
        if click == 1:
            ele.click()
        return ele
