def callback(arg,x):
    print(arg,x)
    arg(x)

#定義一個回呼函式
def handle(num):
    print(100+num)

callback(handle,500)

print('---------------------')

def add(n1,n2):
    return n1+n2
def handle2(abc):
    print("result=",abc)
handle2(add(15,6))

def add2(n1,n2,abc):
    handle3(n1+n2)
def handle3(abc):
    print("result=",abc)
add2(1,6,handle3)