import mysql.connector

## 連線mysql資料庫
con=mysql.connector.connect(
    user='root',
    password='weichih',
    host='54.168.246.147',
    database='mydb'
)
print('資料庫連線成功')
## 建立cursor物件，用來對資料庫下SQL指令
cursor=con.cursor()

## 新增資料
# productName='氣泡水'
# productExtra='氣泡水的備註欄位'
# cursor.execute("insert into product(name,extra) values(%s ,%s)",(productName,productExtra))
# cursor.execute("insert into product(name) values('烏龍茶')")
## 更新資料
# cursor.execute("update product set extra='這是美式的備註喔' where name='美式'")
## 取得單筆資料
# cursor.execute("select * from product where name='拿鐵';")
# data=cursor.fetchone()
# print(data)
# print(data[0],data[1],data[2])
## 取得多筆資料
cursor.execute("select * from product;")
data=cursor.fetchall()
print(data)
print(data[0][2])
# 逐一取得
for row in data:
    print(row[0],row[1],row[2])
con.commit() # 確定執行
con.close() # 關閉資料庫連線