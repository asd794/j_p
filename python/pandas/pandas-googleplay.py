import pandas as pd

data=pd.read_csv("googleplaystore.csv") # 把CSV檔案格式讀成DataFrame
# condition=data['Rating']<=5
# data=data[condition]
print("資料數量",data.shape)
print("資料欄位",data.columns)
print('-----------------------------------')
# print('評分最高20筆',data['Rating'].nlargest(1000).mean(),sep="\n")
print('-----------------------------------')

# data['Installs']=pd.to_numeric(data['Installs'].str.replace("+","").str.replace(",","").replace('Free',''))
# print('平均數',data['Installs'].mean())
# condition=data['Installs']>100000
# print("安裝數量超過100,000的應用程式數量",data[condition].shape[0])

print('-----------------------------------')
print('-----------------------------------')

keyword=input('請出入關鍵字: ')
condition=data["App"].str.contains(keyword,case=False) # case=False 忽略大小寫
print(data[condition])
