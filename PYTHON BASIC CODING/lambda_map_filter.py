#lambda function with one argument.

#we can given n no of arguments
#in lambda function you can write only one expression
'''
adding=lambda x:x+10
print(adding(20))
'''
#normalfun
'''
def isEven(n):
    return n%2==0
print(isEven(23))
'''

#lambdafun
'''
iseven=lambda x:x%2==0
print(iseven(10))
'''
#lambda fun with three arg
'''
mul=lambda x,y,z:x*y/z
print(mul(20,10,2))
'''


#map-arg which function address is using should be only one argn                                                
''''
l=[1,2,33,4]
print(tuple(map(lambda x:x*10,l)))
'''

'''
#space seperated values as output
print(list(map(int,input().split())))

#comma seperated values as output
print(list(map(int,input().split(','))))

'''
#filter with lambda
'''
print(list(filter(lambda x:x%2==0,[2,3,34,45])))
'''
#using filter fun find prime nos in a given list
'''
def isprime(n):
    if n>1:
        for i in range(2,n//2):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
print(list(filter(isprime,[2,3,45,90,18,19])))
'''           
#using filter fun find armstrong nos in a given list
'''
def armstrong(n):
    y=n
    a=len(str(n))
    sum=0
    while y>0:
        rem=y%10
        y//=10
        sum+=rem**a
    if sum==n:
        return True
    else:
        return False
print(list(filter(armstrong,map(int,input().split()))))
'''
#using filter fun find happyno in a given list
'''
def happyno(n):
    while n>9:
        sum=0
        while n>0:
            rem=n%10
            n//=10
            sum+=rem**2
        n=sum
    if n==1 or n==7:
        return True
    else:
        return False

print(list(filter(happyno,map(int,input().split()))))
'''  
#waptp the perfect no in a given list using filter
'''
def perfectno(n):
    sum=0
    for i in range(1,n//2+1):
        if n%i==0:
            sum+=i
    if sum==n:
        return True
    else:
        return False
print(list(filter(perfectno,map(int,input().split()))))
'''
#waptp strong no using filter
'''
def strongno(n):
    sum=0
    y=n
    while y>0:
        rem=y%10
        y//=10
        fact=1
        for i in range(1,rem+1):
            fact*=i
        sum+=fact
    if sum==n:
        return True
    else:
        return False
print(list(filter(strongno,map(int,input().split()))))
'''
#waptp disarium no using filter
'''
def disariumno(n):
    sum=0
    a=len(str(n))
    y=n
    while y>0:
        rem=y%10
        y//=10
        sum+=rem**a
        a-=1
    if sum==n:
        return True
    else:
        return False
print(list(filter(disariumno,map(int,input().split()))))
'''
#waptp harshad no in a given list
'''
def harshadno(n):
    sum=0
    y=n
    while y>0:
        rem=y%10
        y//=10
        sum+=rem
    if n%sum==0:
        return True
    else:
        return False

print(list(filter(harshadno,map(int,input().split())))) 
'''























#waptocheck the given no is prime or not in a single line
'''
in single also we can do this question
'''


#reduce
'''
import functools 
l=[2,100,4,5,7,8]
print(functools.reduce(lambda x,y:x+y,l))
'''
'''
from functools import reduce
l=[10,20,30,40,50]
print(reduce(lambda x,y:x*y,l))
'''
'''
from functools import reduce
l=[10,20,30,40,50]
print("the max no is")
print(reduce(lambda x,y:x if x>y else y,l))
print("the min no is")
print(reduce(lambda x,y:x if x<y else y,l))
'''
'''
from functools import reduce
print("True if they are anagrams else False")
print(reduce(lambda x,y:True if sorted(x)==sorted(y) else False,input().split()))

'''
#flattening of list----but if if example is like this then only it will work
'''                                                                             
from functools import reduce
l=[[10,20],[30,40],[50]]
print(reduce(lambda x,y:x+y,l))
'''














 








































































































































































