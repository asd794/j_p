import pandas as pd

data=pd.DataFrame({   # 5列2欄
    'name':['Amy','Wastson','David','Ema','Frank'],
    'salary':[50000,80000,45000,35000,40000]
},index=['a1','a2','a3','a4','a5'])
print(data)
print('-----------------------------')
print('資料數量',data.size)
print('資料形狀(列,欄)',data.shape)
print('資料索引',data.index)
print('-----------------------------')
print("依據順序取得第2列(ROW/橫向)",data.iloc[1],sep="\n")
print('-----------------------------')
print('根據索引取得第a3列',data.loc["a3"],sep="\n")
print('-----------------------------')
print('取得name欄位',data['name'],sep='\n')
print('-----------------------------')
names=data['name'] # 取得單維度的series資料
print('names轉成大寫',names.str.upper(),sep='\n')
print('-----------------------------')
salaries=data['salary']
print('salary薪水平均值',salaries.mean(),sep='\n') 
print('-----------------------------')
data['ChineseName']=['王小明','羅志祥','熊文銨','羅成員','淑芬'] # 建立新欄位
data['性別']=pd.Series(['男','男','男','男','女'],index=['a1','a2','a3','a4','a5']) # 建立新欄位(比較正式)，需指定index
data['daily']=data['salary']/30
print(data)





