s1={3,4,5} #集合
print(2 not in s1)
s2={4,5,6,7} #集合
s3=s1&s2 #交集
print(s3)
s3=s1|s2 #聯集,不重複取
print(s3)
s3=s1-s2 #差集
print(s3)
s3=s1^s2 #反交集
print(s3)

s=set("Hello") #set(字串)
print(s,"p" in s)

dic={"apple":"蘋果","banana":"香蕉"}
dic["apple"]="大大大蘋果"
# dic=dic+{"watermelon":"西瓜"}
print(dic["apple"])
del dic["banana"]
print("banana" in dic)

dic={x:x**2 for x in s1}
print(dic)