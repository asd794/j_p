import pymongo # 載入pymongo套件
from bson.objectid import ObjectId

## 連線到 MongoDB雲端資料庫
uri = "mongodb+srv://weichih:wtVDTbr4azrGa46E@cluster0.9qo8cqy.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri) 
## 把資料放進資料庫
db=client.mywebsite # 選擇操作mywebsite資料庫
collection=db.users # 選擇操作users集合

result=collection.delete_one({
    "level":3
})
print("實際上刪除的資料有幾筆: ",result.deleted_count)

data=collection.find({"name":"Stanly"})
# print(data)
for i in data:
    print(i)