class Point:
    def __init__(self,n1,n2) :
        self.x=n1
        self.y=n2
p1=Point(3,4)  # 建立第一個實體物件
print(p1.x,p1.y)
p2=Point(5,6)  # 建立第二個實體物件
print(p2.x,p2.y)

class FullName:
    def __init__(self,first,last) :
        self.fisrt=first
        self.last=last
name1=FullName("Xiao Ming","Wang")
print(name1.fisrt,name1.last)
name2=FullName("fisrt","last")
print(name2.fisrt,name2.last)