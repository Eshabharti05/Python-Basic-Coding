 #function with arg
'''
def add(a,b):
    print(a+b)
n=int(input())
m=int(input())
add(n,m)
'''
#positional or mandatory arguments
'''
def add(a,b):
    print('a value is',a)
    print('b value is',b)
    print('sum is',a+b)
add(1,5)
'''
#keyword arguments
'''
def add(a,b):
    print('a value is',a)
    print('b value is',b)
    print('sum is',a+b)
add(a=1,b=5)
'''


'''
#restricted arguments
#(positional (/))
def add(a,b,/):
    print('a value is',a)
    print('b value is',b)
    print('sum is',a+b)
add(1,5)
#(keyword(*))
def add(*,a,b):
    print('a value is',a)
    print('b value is',b)
    print('sum is',a+b)
add(a=11,b=5)
'''

#default arguments
'''
def add(a=10,b=9):
    print("sum",a+b)
add(12)
add(1,1)
add()
'''

#variable length arguments
'''
def add(*args):
    print(args)
    print(type(args))
    sum=0
    for i in args:
        sum+=i
    print(sum)
add()#0
#add(100)#100
#add(1,233)#234
'''
'''
def add(*esha):
    print(esha)
    sum=0
    for i in esha:
        sum+=i
    print(sum)
add(11)
add(11,45)
add()
'''




#variable length keyword arguments(**kwargs)
'''
def add(**esha):
    print(esha)
    sum=0
    for i in esha:
        sum+=esha[i]
    print(sum)
add(a=11,b=45)
'''
#return type
'''
def fun():
    return 10
fun()#for this no output
print(fun())
a=fun()
print(a)
'''
'''
def lifeCycle(age):
    if age in range(0,13):
        return 'Child'
    elif age in range(13,20):
        return 'Teenage'
    elif age in range(20,50):
        return 'Adult'
    else:
        return 'Legends'
lifeCycle(20)#no output
a=lifeCycle(12)
print(a)

'''


#check if  a number is prime or not
'''
def prime(n):
    fact=0
    for i in range(1,n//2+1):
        if n%i==0:
            fact+=1
    if fact<3:
        return "yes prime"
    else:
        return "not prime"
print(prime(80))
'''
'''
def prime(n):
   if n>1:
       for i in range(2,n//2+1):
           if n%i==0:
               return "not a prime"
       else:
            return "yes prime"
   else:
        return "not a prime"
print(prime(8))
'''
#check prime no in a given range
'''
def prime(n):
   if n>1:
       for i in range(2,n//2+1):
           if n%i==0:
               return False
       else:
            return True
   else:
        return False

def fun(ll,ul):
    for i in range(ll,ul+1):
        if prime(i):
            print(i)
ll=int(input())
ul=int(input())
fun(ll,ul)
'''
#even or not
'''
def even(n):
    if n%2==0:
        return "yes even no"
    else:
        return "not a even no"
print(even(3))
'''
#even no in a given range
'''
def iseven(n):
    if n%2==0:
        return True
    else:
        return False
def fun(ll,ul):
    for i in range(ll,ul+1):
        if iseven(i):
            print(i)
ll=int(input())
ul=int(input())
print(fun(ll,ul))
'''

#within a given string count the frequency of each element
'''
def freq(n):
    l={}
    for i in n:
        if i not in l:
            l[i]=1
        else:
            l[i]+=1
    print(l)

print(freq("eshjjjhhhaaa"))
'''

#wapt check whether a no is  palindrome no or not
'''
def reverse(n):
    y=n
    rev=0
    while y>0:
        rem=y%10
        rev=rev*10+rem
        y//=10
    if rev==n:
        return "yes palindrome no"
    else:
        return "not a palindrome no"

print(reverse(101))
        
'''
#waptp palindrome no in a given range
'''
def isreverse(n):
    y=n
    rev=0
    while y>0:
        rem=y%10
        rev=rev*10+rem
        y//=10
    if rev==n:
        return True
    else:
        return False

def fun(ll,ul):
    for i in range(ll,ul+1):
        if isreverse(i):
            print(i)
ll=int(input())
ul=int(input())
print(fun(ll,ul))
'''
#armstrong no or not
'''
def armstrong(n):
    a=len(str(n))
    y=n
    sum=0
    while y>0:
        rem=y%10
        y//=10
        sum+=rem**a
    if sum==n:
        return "yes armstrong no"
    else:
        return "not an armstrong no"

print(armstrong(153))
'''
#arms in a given range
'''
def armstrong(n):
    a=len(str(n))
    y=n
    sum=0
    while y>0:
        rem=y%10
        y//=10
        sum+=rem**a
    if sum==n:
        return True
    else:
        return False

def fun(ll,ul):
    for i in range(ll,ul+1):
        if armstrong(i):
            print(i)
ll=int(input())
ul=int(input())
print(fun(ll,ul))
'''

#wap to find every second prime no in a given range
'''
def prime(n):
   if n>1:
       for i in range(2,n//2+1):
           if n%i==0:
               return False
       else:
            return True
   else:
        return False

def fun(ll,ul):
    c=0
    for i in range(ll,ul+1): 
        if prime(i):
            c+=1
            if c%2==0:
                print(i)
print(fun(2,11))        
'''     
#waptp harshad no in a given range
'''
def harshad(n):
    y=n
    sum=0
    while y>0:
        rem=y%10
        y//=10
        sum+=rem
    if n%sum==0:
        return True
    else:
        return False
    
def fun(ll,ul):
    for i in range(ll,ul+1):
        if harshad(i):
            print(i)
ll=int(input())
ul=int(input())
print(fun(ll,ul))
'''
#disarium no in a given range
'''
def disarium(n):
    y=n
    a=len(str(n))
    sum=0
    while y>0:
        rem=y%10
        y//=10
        sum+=rem**a
        a-=1

    if sum==n:
        return True
    else:
        return False

def fun(ll,ul):
    for i in range(ll,ul+1):
        if disarium(i):
            print(i)
ll=int(input())
ul=int(input())
print(fun(ll,ul))
'''
#perfect no in a given range
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

def fun(ll,ul):
    for i in range(ll,ul+1):
        if perfectno(i):
            print(i)
ll=int(input())
ul=int(input())
print(fun(ll,ul))
'''
#strong no or not----1!+4!+5!=1+24+120=145
'''
def strongno(n):
    y=n
    sum=0
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

def fun(ll,ul):
    for i in range(ll,ul+1):
        if strongno(i):
            print(i)
ll=int(input())
ul=int(input())
print(fun(ll,ul))
'''
#convert an integer into binary no
'''
def binaryno(n):
    y=n
    bno=""
    while y>0:
        rem=y%2
        y//=2
        bno=str(rem)+bno
    return bno

def fun(ll,ul):
    for i in range(ll,ul+1):
        print(binaryno(i))
        
ll=int(input())
ul=int(input())
fun(ll,ul)
'''
#convert binary no to integer
'''
num=1011
position=0
res=0
while num>0:
    rem=num%10
    res+=rem*2**position
    num=num//10
    position+=1
print(res)
'''


#this program is incomplete
'''
def integer(n):
    pos=0
    res=0
    while n>0:
        rem=n%10
        n//=10
        res+=rem*2**pos
    return res

def fun(ll,ul):
    for i in range(ll,ul+1):
        bv=input()
        
        print(integer(bv))
ll=int(input())
ul=int(input())
fun(ll,ul)
'''



#important question
'''
s="AABCAAYDABAC"
k=4
new=""
for ip in range(len(s)):
    if s[ip] not in new:
        new+=s[ip]
    if (ip+1)%k==0:
        print(new)
        new=""
'''
#happy number

n=int(input())
if n>9:
    sum=0
    while n>0:
        rem=n%10
        n//=10
        sum+=rem**2
    n=sum
if n==1 or n==7:
    print("happy no")
else:
    print('nota happyno')
   


























        
        
    

    



































































'''
n=111
power=1
res=0
while n!=0:
    rem=n%10
    n//=10
    res=res+rem*power
    power*=2
print(res)
'''



#fibbonacci series
'''
def fibonacci(n):
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the number of terms:"))

for i in range(n):
    print(fibonacci(i))

'''
'''
def fibo(fv=0,sv=1,n=10):
    if n==1:
        print(fv)
    elif n==2:
        print(fv,sv)
    else:
        print(fv)
        print(sv)
        for i in range(n-2):
            tv=fv+sv
            print(tv)
            fv,sv=sv,tv
fibo()
'''
'''
def fibo(fv=0,sv=1,n=10):
    for i in range(n):
        print(fv)
        fv,sv=sv,fv+sv
fibo()
'''






#paliprime no 
'''
def reverse(n):
    dummy=n
    rev=0
    while dummy>0:
        rem=dummy%10
        rev=rev*10+rem
        dummy//=10
    return rev
    
def isPrime(n):
    if n>1:
        for i in range(2,(n//2)+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False

def isPaliPrime(n):
    rev=reverse(n)
    if isPrime(n) and rev==n:
        return True
    else:
        return False

def fun(ll,ul):
    for i in range(ll,ul+1):
        if isPaliPrime(i):
            print(i)
            
fun(1,1000)
'''


#emrip no
''' emirp is a no. which is prime and as well as its
reverse also prime, but it should not be palindrome eg=13,199,71,17'''
'''

def isPrime(n):
    if n>1:
        for i in range(2,(n//2)+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False

    
def reverse(n):
    y=n
    rev=0
    while y>0:
        rem=y%10
        y//=10
        rev=rev*10+rem
    return rev

def isEmrip(n):
    rev=reverse(n)
    if isPrime(n) and isPrime(rev) and rev!=n:
        return True
    else:
        return False

def fun(ll,ul):
    for i in range(ll,ul+1):
        if isEmrip(i):
            print(i)
            
fun(1,1000)

'''



























































































































































































