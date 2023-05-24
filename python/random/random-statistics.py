import random   # 亂數模組
import statistics as stat # 統計模組

data=random.choice([1,5,6,10,20])   # 隨機取1個
print(data)
data=random.sample([1,5,6,10,20],3) # 隨機取3個
# data.append(500)
print(data)
for i in data:
    print(i)


print("--------------------")
n=1
# y=0
array=[]
while n<21:
    data=random.randint(1,20)   # 隨機取範圍1~20
    # print(data) # 測
    if data in array:
        continue
    else:
        array.append(data)
        n+=1
print("array長度:",len(array),array)
data=random.randrange

array2=[]
for i in range(1,21):
    array2.append(i)
random.shuffle(array2)  # 隨機調換順序
print("array2長度:",len(array2),array2)
print("--------------------")
data=random.random()    # 取 0.0 ~ 1.0 亂數
print(data)
data=random.uniform(0.0,1.0) #  0.0 ~ 1.0 亂數
print(data)
print("--------------------")
for i in range(5):
    data=random.normalvariate(100,10)   # 平均數 100, 標準差 10, 得到的資料多數在 90 ~ 110 之間
    print(data)
print("--------------------")

data=stat.mean([1,2,3,4,5,6,7,8,9,10])  # 平均數
print(data)
data=stat.median([1,6,8,10,55]) # 中位數
print(data)
data=stat.stdev([1,2,5,5,10,20]) # 標準差
print(data)
