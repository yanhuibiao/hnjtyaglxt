import numpy as np
import pandas as pd
data = pd.read_excel(r"C:\Users\77238\PycharmProjects\hnjtygglxt\app\data\data.xlsx")
data_list= list(data.groupby("ID"))
print(data_list[0][1])
