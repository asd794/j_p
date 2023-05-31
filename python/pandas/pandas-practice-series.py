import pandas as pd

data=pd.Series([10,50,-5,40,20],index=['a',"b","c",'d','e'])
print("資料索引",data.index) # 資料索引
print("資料數量",data.size) # 資料數量
print("資料型態",data.dtype) # 資料型態
print(data.dtype) # 資料型態
print(data["a"],data[0]) # 依索引(index)或是順序搜尋
print("最大值",data.max())
print("總和",data.sum())
print("標準差",data.std())
print("中位數",data.median())
print("最大三個數\n",data.nlargest(3))
print("最小三個數\n",data.nsmallest(3))

print('-------------------------------------------')

data2=pd.Series(["熊文銨","Python",'還錢' ,'paNDas'])
print(data2.str.lower()) # 全變小寫
print(data2.str.upper()) # 全變大寫
print(data2.str.len()) # 計算每一個字串的長度
print(data2.str.cat(sep='~')) # 把全部字串用~串起來
print(data2.str.contains("p")) # 搜尋字串是否包含p，布林值返回結果
print(data2.str.replace('a','發大財')) # 取代字串a變成發大財