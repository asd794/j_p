## 裝飾器工廠

def myFactory(base):
    def myDeco(cb):
        def run():
            print('裝飾器內部函式',base)
            result=base*2
            cb(result)
        return run
    # print('裝飾器內部函式777',base)
    return myDeco
@myFactory(3)
def test(res):
    print("普通函式內",res)
test()

print('----------------------------')

def myFactory2(int):
    def myDeco2(cb):
        def run():
            sum=0
            for i in range(int+1):
                sum+=i
            print("裝飾器函式內")
            result=sum
            cb(result)
        return run
    return myDeco2
@myFactory2(100)
def test2(resu):
    print("普通函式內",resu)
test2()
