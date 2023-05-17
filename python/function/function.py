def add (n1,n2):
    sum=n1+n2
    print(sum)
    return sum

def funfor(max):
    sum=0
    for i in range(1 , max+1):
        sum+=i
    return sum

value=add(55,99)
print(value*2)

sum=funfor(10)+funfor(11)
print(sum)


