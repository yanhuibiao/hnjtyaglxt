import time
import pytest
from app.utils import Apptest

import pandas as pd

data = pd.read_excel(r"C:\Users\77238\PycharmProjects\hnjtygglxt\app\data\data.xlsx")
data_list = list(data.groupby("ID"))
# print(data_list[0][1])

# Apptest.element(By.ID, "com.vondear.onemap:id/ed_unit_code", 1, 1, "431011211")
# Apptest.element(By.ID,  "com.vondear.onemap:id/ed_password", 1 , 1, "3edc$RFV1")
# Apptest.element(By.ID, "com.vondear.onemap:id/ed_collect_name", 1, 1, "捞逼刘")
# Apptest.element(By.ID, "com.vondear.onemap:id/ed_collect_phone", 1, 1, "13012341234")
# Apptest.element(By.ID, "com.vondear.onemap:id/btn_login",send_keys=0,click=1)
time.sleep(0.5)


class Test01:
    def teardown_class(self):
        Apptest.quit_driver()

    @pytest.mark.parametrize("i", [1, 2, 3, 4])
    def test_01(self, i):
        data = data_list[i][1]
        for j in data.index:
            print("haha")
            Apptest.element(data.by[j], data.find_values[j], data.clear[j], data.send_keys[j], data.send_key_values[j],
                            data.click[j])
    assert "密码错误" == "密码错误"
