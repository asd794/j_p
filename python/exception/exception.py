## 例外處理情境

# data=input("請輸入一個數字: ")
# try:
#     num=int(data)
# except Exception:
#     num=0
# num=num*2
# print(num)

num=0
while True:
    data=input("請輸入一個數字: ")
    try:
        num=int(data)
        break
    except Exception:
        print('錯誤, 輸入格式不是數字, 請重新輸入。')
num=num*2
print(num)
    
