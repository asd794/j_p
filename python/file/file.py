# file=open("data.txt",mode="w",encoding="utf-8")
# file.write("Hello File\n大家好")
# file.close

with open("data.txt",mode="w",encoding="utf-8") as file:
    file.write("1\n2\n3")

array=[]
index=0

with open("data.txt",mode="r",encoding="utf-8") as file:
    data=file.read()
    for line in file:
        # print(file.readlines())
        # print(array[0])
        print(line)
        array.append(line)

        # print(line)


print(array)
