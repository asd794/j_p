import pymongo # 載入pymongo套件

# 連線到MongoDB雲端資料庫


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
db=client.test # 選擇操作test資料庫
collection=db.users # 選擇操作users集合
# 把資料新增在集合中
collection.insert_one({
    "name":"熊問安",
    "gender":"男"
})

print('資料新增成功')