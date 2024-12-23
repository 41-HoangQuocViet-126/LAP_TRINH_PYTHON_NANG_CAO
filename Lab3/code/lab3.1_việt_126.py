import pandas as pd

DataFrame_stock1 = pd.read_csv('D:\\17A3DHKL\\Lab3\\DATA\\stocks1.csv')
print(DataFrame_stock1)

print("5 dòng đầu tiên của DataFrame Stock1 là:\n",DataFrame_stock1.head(5))
print("Kiểu dữ liệu của DataFrame Stock1 là:\n",DataFrame_stock1.dtypes)
print("Thông tin tổng quan của Stock1 là:\n",DataFrame_stock1.info())