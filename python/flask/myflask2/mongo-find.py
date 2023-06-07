import pymongo # 載入pymongo套件
from bson.objectid import ObjectId

## 連線到 MongoDB雲端資料庫
uri = "mongodb+srv://weichih:wtVDTbr4azrGa46E@cluster0.9qo8cqy.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri) 
## 把資料放進資料庫
db=client.mywebsite # 選擇操作mywebsite資料庫
collection=db.users # 選擇操作users集合
cursor=collection.find()
for i in cursor:
    print(i)

print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
## 單筆篩選
# doc=collection.find_one({
#     "email":"3cm@gmail.com"
# })

## 複合單筆篩選條件
# doc=collection.find_one({
#     "$and":[
#         {"email":"bin@gmail.com"},
#         {'password':'binbin55667'}
#     ]
# })

## 多筆篩選or +篩選sort
doc=collection.find({
    "$or":[
        {"name":"彬彬"},
        {'password':'binbin5566'},
        {"level":1}
        ]
    },sort=[
        ("level",pymongo.DESCENDING) # 大到小排序
])
print('大到小排序')
for i in doc:
    print(i)
print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

doc=collection.find(
    {"$or":[{"name":"彬彬"},{'level':1}]},
    sort=[('level',pymongo.ASCENDING)] # 小到大排序
)
print('小到大排序')
for i in doc:
    print(i)
# print('取得資料欄位',doc)
print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('篩選level>=3')
doc=collection.find(
    {'level':{'$gte':3}}
)
for i in doc:
    print(i) 
