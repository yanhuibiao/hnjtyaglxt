import time

import pytest
from appium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",
                          {"platformName": "android",  # 表示的是android  或者ios
                           "platformVersion": "7.1.2",  # 表示的是平台系统的版本号
                           "deviceName": "emulator-5554",  # 表示的是设备的ID名称（如果只有一个设备可以用****来代替）
                           "appPackage": "com.vondear.onemap",  # 表示app的包名
                           "appActivity": ".activity.ActivityLogin",  # 表示的是app的界面名
                           "noReset": True,  # 用来记住app的session，如果有登陆或做过初始化的操作，为True时，后面不需要再操作
                           "resetKeyboard": True,  # 重置设备的输入键盘
                           "unicodeKeyboard": True})  # 采用unicode编码输入，可以输入中文
#driver.implicitly_wait(5)  #隐式等待
#driver.start_activity("com.baidu.homework", ".activity.index.IndexActivity")  #打开app
driver.find_element(By.ID, "com.vondear.onemap:id/ed_unit_code").clear().send_keys("431011211")
driver.find_element(By.ID, "com.vondear.onemap:id/ed_password").clear().send_keys("3edc$RFV")
driver.find_element(By.ID, "com.vondear.onemap:id/ed_collect_name").clear().send_keys("捞逼刘")
driver.find_element(By.ID, "com.vondear.onemap:id/ed_collect_phone").clear().send_keys("13012341234")
driver.find_element(By.ID, "com.vondear.onemap:id/btn_login").click()
time.sleep(3)
driver.find_element(By.ID, "com.vondear.onemap:id/rb0").click()
driver.quit()
