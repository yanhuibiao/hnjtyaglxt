from appium import webdriver as aw
from selenium import webdriver as sw
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import json

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


class Get_driver:
    driver = None

    @classmethod
    def get_web_driver(cls):
        if cls.driver is None:
            cls.driver = sw.Edge()
            cls.driver.get("http://10.200.255.6:8090/login")
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(5)
        return cls.driver

    @classmethod
    def get_app_driver(cls):
        if cls.driver is None:
            cls.driver = aw.Remote(command_executor, desired_capabilities)
            cls.driver.implicitly_wait(5)
            # print(cls.driver.current_activity)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver is not None:
            cls.driver.quit()
            cls.driver = None


# 定义输入文本前先清除的函数
def send_text(element, send_keys_values):
    element.clear()
    element.send_keys(send_keys_values)


# 定义隐式等待函数
def get_element(driver, by_value):
    element = WebDriverWait(driver, 10, 1).until(lambda x: x.find_element(*by_value))
    return element


# 获取弹出框元素信息
def get_alert():
    a = Get_driver()
    alter = a.get_web_driver().switch_to.alert
    return alter


# 获取data中的数据进行参数化
def get_app_data():
    # f = open("./appv1/data/data.json", "r", encoding="utf8")
    with open("./appv1/data/data.json", "r", encoding="utf8") as f:
        data = json.load(f)
    list_data = []
    for i in data:
        list_data.append(tuple(i.values()))
    return list_data
