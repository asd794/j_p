# 定義裝飾器
def myDeco(callback):
    def run():
        print("裝飾器中的程式碼")
        callback(99) # 這個回呼函式，其實就是被裝飾的普通函式
    return run

# 使用裝飾器
@myDeco 
def test(n):
    print("普通函式的程式碼",n)

test()

print('---------------------------------')

def calculate(callback):
    def run():
        sum=0
        for i in range(51):
            sum+=i
        print(sum)
        callback(sum) # 這個回呼函式，其實就是被裝飾的普通函式
    return run

@calculate
def test2(result):
    print('這是在普通函式的程式碼',result)
@calculate
def test3(result):
    print('result = ',result)
test2()
test3()