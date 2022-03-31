import time

from selenium.webdriver.common.by import By

from app.utils import Apptest

Apptest.element(By.ID, "com.vondear.onemap:id/ed_unit_code", 1, 1, "431011211")
Apptest.element(By.ID,  "com.vondear.onemap:id/ed_password", 1 , 1, "3edc$RFV1")
Apptest.element(By.ID, "com.vondear.onemap:id/ed_collect_name", 1, 1, "捞逼刘")
Apptest.element(By.ID, "com.vondear.onemap:id/ed_collect_phone", 1, 1, "13012341234")
Apptest.element(By.ID, "com.vondear.onemap:id/btn_login",click=1)
time.sleep(0.5)
expect = Apptest.element(By.XPATH,"//*[contains(@text,'登录失败')]").text
print(expect)

class Test01:
    def test_01(self):
        print(expect)
        assert "登录失败" in expect
Apptest.quit_driver()
