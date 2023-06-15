from flask_bcrypt import Bcrypt
bcrypt=Bcrypt()

password="123456"

hash_password=bcrypt.generate_password_hash(password=password)
print(hash_password)

check_password=bcrypt.check_password_hash('$2b$12$jPV/w.ME3E4L4w6ep2YrNeaHJErL5lAPhWwk610yDl8twSmcFrhFO',"nl")
print(check_password)

# dic={'email':'123@gmail.com','password':'123456'}
# print(dic['email']=='123@gmail.com')


array=[]
name='Hel lo'
sum=1
# print(name[0])
# print(len(name))
# for i in name:
#     print(i)
name2=''
num='10'
for i in range(len(num)-1,-1,-1):
    print(num)

print(name.count("l"))

num=10
if num==10:
    print('你好')
elif num>1:
    print('你好2')


abc=['sab','aaaaa','bs']
print(len(abc[1]))
a=1
b=1
c=1
if a==b==c:
    print('HI')
print(abc[0][1])

compare=[]
strs= ["flower","flow","flight"]
for i in range(len(strs[0])):
    if len(strs[1])>i:
        if strs[0][i]==strs[1][i]:
            compare.append(strs[0][i])
        else:
            break
    else:
        break
for i in compare

print(compare)