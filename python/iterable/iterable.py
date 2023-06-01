array=[90,5,7,1,0,4,9,1,2,3,5,-1,55,-60]
n=0
nAdd=0
for OriginNum in range(len(array)):
    for compareNum in range(len(array)-n):
        oriNumber=array[OriginNum]
        nAdd=compareNum+n
        if array[OriginNum]>array[nAdd]:
            array[OriginNum]=array[nAdd]
            array[nAdd]=oriNumber
    n+=1
print(array)

