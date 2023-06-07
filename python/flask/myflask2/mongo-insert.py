import pymongo # 載入pymongo套件
from bson.objectid import ObjectId

## 連線到 MongoDB雲端資料庫
uri = "mongodb+srv://weichih:wtVDTbr4azrGa46E@cluster0.9qo8cqy.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri) 
# ## Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

## 把資料放進資料庫
db=client.mywebsite # 選擇操作mywebsite資料庫
collection=db.users # 選擇操作users集合
## 把資料新增在集合中
# result=collection.insert_one({
#     "name":"薛弘偉",
#     "email":["dinter@gmail.com","ddinter@gmail.com"],
#     "gender":"男",
#     "level":3
# })
# print('資料新增成功')
# print(result.inserted_id) # 印出新增資料的編號

## 一次新增多筆資料到集合中，取得新增資料編號
# result=collection.insert_many([{
#     "name":"Stanly",
#     "email":"stanley@stanly.com",
#     "gender":"男",
#     "level":2
# },{
#     "name":"Dinter",
#     "email":"Dinter@dinter.com",
#     "gender":"男",
#     "level":3
# }])
# print('資料新增成功')
# print(result.inserted_ids) # 印出新增資料的編號

## 取得集合中的第一筆文件資料
data=collection.find_one(ObjectId("647ff507e0629b3d08de6220"))
print(data)

## 一次取得多筆文件資料
cursor=collection.find()
print(cursor)
for i in cursor:
    # print(i)
    print(i["email"])
