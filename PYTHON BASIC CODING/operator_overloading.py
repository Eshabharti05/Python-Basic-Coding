class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
        self.area=l*b
    def __gt__(self,sec):
        return self.area>sec.area
r1=Rectangle(2,3)
r2=Rectangle(3,7)
print(r2>r1)

class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def __gt__(self,sec):
        area1=self.l*self.b
        area2=sec.l*sec.b
        return area1>area2
r1=Rectangle(2,3)
r2=Rectangle(3,7)
print(r2>r1)
