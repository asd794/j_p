# 可疊代資料，字串、列表、集合(不按照順序)、字典
abc={"a":"你好","z":123,"f":"測試"}
for i in abc:
    print(abc[i])

print('-------------------------------------')    

# 內建函式
# max ,min ,sorted  (可疊代資料)
result=max([99,40,-5,40,58,100,0])
print(result)
result=max({2,4,6,1,20})
print(result)
result=max('ksfzxd')
print(result)
result=max({"a":"你好","x":123,"f":"測試"})
print(result)

print('-------------------------------------') 

result=sorted([99,40,-5,40,58,100,0])
print(result)
result=sorted({2,4,6,1,20})
print(result)
result=sorted('ksfzxd')
print(result)
result=sorted({"a":"你好","x":123,"f":"測試"})
print(result)
result=sorted((99,40,-5,40,58,100,0))
print(result)

print('-------------------------------------')

# sorted是複製一份進行排序 , sort()是直接在原list排序(所以沒有回傳)

abc=[99,40,-5,40,58,100,0]
print(abc.sort())

