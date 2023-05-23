import re ,json

# file=open("data.txt",mode="w",encoding="utf-8")
# file.write("Hello File\n大家好")
# file.close

with open('test.txt',encoding='utf-8',mode='w') as test:
    for i in range(10):
        test.write(str(i))
        test.write("\n")
with open('test.txt' ,mode='r',encoding='utf-8') as test:
    # data=test.read()
    # print(data)
    for line in test:
        print(line)


with open("data.txt",mode="w",encoding="utf-8") as file:
    file.write("1\n19\n30")
array=[]
sum=0
with open("data.txt",mode="r",encoding="utf-8") as file:
    # data=file.read()  # 一次將全部資料放到data
    # print(data)
    for line in file:   # 一行一行印出
        # print(file.readlines())
        # print(array[0])
        sum+=int(line)
        print(line)
        if '\n' in line:    # 判斷是否有\n
            array.append(re.sub('\n','',line))  # 刪除\n
            print('yes')
        else:
            print('no')
            array.append(line)
print(array)
print(sum)
abc='NLNLXD'
print(re.sub('LN','',abc))

with open("config.json",mode="r") as file:
    data=json.load(file)
print("name",data["name"])
print("version",data["version"])
