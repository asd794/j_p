# file=open("data.txt",mode="w",encoding="utf-8")
# file.write("Hello File\n大家好")
# file.close

with open("data.txt",mode="w",encoding="utf-8") as file:
    file.write("1\n19\n30")

array=[]
sum=0
with open("data.txt",mode="r",encoding="utf-8") as file:
    # data=file.read()
    # print(data)
    for line in file:
        # print(file.readlines())
        # print(array[0])
        sum+=int(line)
        print(line)
        array.append(line)

print(array)
print(sum)
