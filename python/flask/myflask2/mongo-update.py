import pymongo # 載入pymongo套件
from bson.objectid import ObjectId

## 連線到 MongoDB雲端資料庫
uri = "mongodb+srv://weichih:wtVDTbr4azrGa46E@cluster0.9qo8cqy.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri) 
## 把資料放進資料庫
db=client.mywebsite # 選擇操作mywebsite資料庫
collection=db.users # 選擇操作users集合

## 更新集合一筆資料------------------------
# result=collection.update_one({
#     "email":"stanley@stanley.com"
# },{
#     "$set":{
#         "password":"5566" # 如果無password欄位，會新增一個新的欄位
#     }
# })

# result=collection.update_one({
#     "email":"stanley@stanley.com"
# },{
#     "$unset":{ # 刪除欄位
#         "password":""
# }})

# result=collection.update_one({
#     "email":"toyz@gmail.com"
#     },{
#         "$inc":{ # 欄位值加10
#             "level":10
#     }})

# result=collection.update_one({
#     "email":"toyz@gmail.com"
#     },{
#         "$mul":{ # 欄位值乘0.5
#             "level":0.5
#     }})

## 更新集合多筆資料------------------------
result=collection.update_many({
    "email":"stanley@gmail.com"
},{
    "$set":{
        "gender":"不詳吧"
}})


print("符合條件的文件數量",result.matched_count)
print("實際更新的文件數量",result.modified_count)
cursor=collection.find()
for i in cursor:
    print(i)