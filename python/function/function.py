def add (n1,n2):
    sum=n1/n2
    print(sum)
    return sum

def funfor(max):
    sum=0
    for i in range(1 , max+1):
        sum+=i
    return sum

def say(*msgs):
    for i in msgs:
        print(i)
    return "緊張囉"

value=add(2,1)
print(value*2)
add(n2=2,n1=1)

sum=funfor(10)+funfor(11)
print(sum)

print(say("說話",222,"HI"))

