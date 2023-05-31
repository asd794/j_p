import pandas as pd

data=pd.read_csv("googleplaystore.csv") # 把CSV檔案格式讀成DataFrame
condition=data['Rating']<=5
data=data[condition]
print("資料數量",data.shape)
print("資料欄位",data.columns)
print('-----------------------------------')
print('評分最高20筆',data['Rating'].nlargest(20),sep='\n')