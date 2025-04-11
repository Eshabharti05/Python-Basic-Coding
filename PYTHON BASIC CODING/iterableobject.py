'''
class Fibbo:
    def __init__(self,fv,sv,n):
        self.fv=fv
        self.sv=sv
        self.n=n
    def __iter__(self):
        print("iter called")
        self.i=1
        return self
    def __next__(self):
        print("next called")
        if self.i<=self.n:
            res=self.fv
            self.fv,self.sv=self.sv,self.fv+self.sv
            self.i+=1
            return res
            
        raise StopIteration
res=Fibbo(1,2,10)
for i in res:
    print(i)
'''
'''
class Power:
    def __init__(self,ll,ul,up=1):
        self.ll=ll
        self.ul=ul
        self.up=up
    def __iter__(self):
        print("iter called")
        self.i=self.ll
        return self
    def __next__(self):
        print("next called")
        if self.i<self.ul:
            res=self.i**2
            self.i+=self.up
            return res
        raise StopIteration

pow=Power(1,6)
for i in pow:
    print(i)
'''
class Div:
    def __init__(self,ll,ul,up=1):
        self.ll=ll
        self.ul=ul
        self.up=up
    def __iter__(self):
        print("iter called")
        self.i=self.ll
        return self
    def __next__(self):
        print("next called")
        if self.i<self.ul:
            res=self.i/2
            self.i+=self.up
            return res
        raise StopIteration

pow=Div(1,6)
for i in pow:
    print(i)


            
            
            
        
            
            
