# 定義建立生成器函式
def test():
    print('階段一')
    yield 6+4
    print('階段二')
    yield 66
    # print('-----------2------------')
def generateEven():
    num=0
    yield num
    num+=2
    yield num
    num+=2
    yield num
def generateEven2(input):
    num=0
    while num<input:
        yield num
        num+=2

# 呼叫並回傳生成器
gen=test()
# print(gen)

# 搭配for迴圈中使用
for i in gen:
    print(i)

print('-----------------------')

evenGenerator=generateEven()
for i in evenGenerator:
    print(i)
    
print('-----------------------')

evenGenerator2=generateEven2(11)
for i in evenGenerator2:
    print(i)
