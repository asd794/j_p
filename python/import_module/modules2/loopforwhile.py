# n=0
# while n<5:
#     if n==3:
#         break
#     print(n)
#     n+=1
# print(n)

array=[]
print(len(array))
index=0
for x in [0,1,2,3]:
    if x%2==0:  #mod2 偶數
        continue
    array.insert(index,x)
    index+=1
print(array)

sum=0
for i in range(11):
    sum+=i
else:   #迴圈結束前印出print(sum)
    print(sum)

n=int(input("請輸入一個正整數: "))
for i in range(n):
    if i*i==n:
        print(n,"的平方根為",i)
        break #braek強制結束迴圈不回執行else
else:
    print(n,"沒有平方根")
