# n=1
# sum=0
# while n<=10:
#     print(n)
#     sum+=n
#     n+=1
# print(sum)
sum=0
for i in range(1,11):
    sum+=i
print(sum)

for i in [3,5,1]:
    print(i)

for i in "[3,5,1]\"":
    print(i)

for i in range(5):
    print(i)

for i in range(2):
    print(i)


y=0
long=len("Hello")
array=["none"]*long
for i in "Hello":
    if i in array:
        y+=1
        continue
    array[y]=i
    y+=1

print(array)

