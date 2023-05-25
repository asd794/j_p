class Point:
    def __init__(self,x,y) :
        self.x=x
        self.y=y
    def show(self):
        print(self.x,self.y)
    def distance(self,targetX,targetY):
        return (((self.x-targetX)**2)+((self.y-targetY)**2))**0.5

p=Point(5,6)
p.show()
# Point.show()  # 不能直接呼叫類別
result=p.distance(0,0)
print(result)

class file:
    def __init__(self,name):
        self.name=name
        self.data=None
    def open(self):
        self.data=open(self.name,mode="r",encoding="utf-8")
        # print(self.data.read())
    def read(self):
        return self.data.read()
f1=file("test1.txt")
f1.open()
data=f1.read()
print(data)
