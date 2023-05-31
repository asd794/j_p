import pandas as pd

data=pd.Series([30,15,20])
condition=data>18
print(condition)
filterdData=data[condition]
print(filterdData)
print('----------------------------')
data=pd.Series(['您好','PythoN','pANDAs'])
condition=data.str.contains('好')
print(condition)
filterdData=data[condition]
print(filterdData)
print('----------------------------')
data=pd.DataFrame({   # 5列2欄
    'name':['Amy','Wastson','David','Ema','Frank'],
    'salary':[50000,80000,45000,35000,40000]
})
condition=data['salary']>=50000
filterdData=data[condition]
print(filterdData)