import pandas as pd # 載入pandas模組

## Series
data=pd.Series([20,10,15]) # 建立Series
# print(data)
# array=[1,2,3,4,5,6,7,8,9,10]
# print(array)
# data2=pd.Series(array)
# print(len(data2))

print("Max",data.max())
print("Median",data.median())
print(data*2)

print(data==20)

print('-------------------------------------------')
## DataFrame
data=pd.DataFrame({
    "name":["Amy","Allen","Justin","Amelia","Jeff"],
    "salary":[30000,50000,35000,60000,70000]

})
print(data)
print(data['name']) # 取得特定欄位
print(data.iloc[0]) # 取得特定的列