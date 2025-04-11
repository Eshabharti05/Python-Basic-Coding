
#find sum of digits in a given no
'''
n=int(input())
sum=0
dummy=n
while dummy>0:
    rem=dummy%10
    n=dummy//10
    sum+=rem
print(sum)
print(dummy)
print(n)

  '''  
#wap to print the sum of individual digits of a given no is even or not
'''
n=int(input())
sum=0
while n>0:
    rem=n%10
    n=n//10
    sum+=rem
if sum%2==0:
    print(sum,"sum is even")
else:
    print(sum," sum is odd")
 '''   
#wap to print given no is armstrong no or not
#if the no is equals to
'''
n=int(input())
sum=0
dummy=n
a=len(str(dummy))

while dummy>0:
    rem=dummy%10
    sum+=(rem**a)
    dummy//=10
    
if sum==n:
    print("yes armstrong no")
else:
    print("not an armstrong no")
    
'''
#wap to print whether a no is disarium or not.wg=135 1**1+3**2+5**3=135 to the power of their positions
'''
n=int(input())
sum=0
a=len(str(n))
dummy=n
while dummy>0:
    rem=dummy%10
    dummy//=10
    sum+=rem**(a)
    a-=1
if sum==n:
    print("yes disarium")
else:
    print("not disarium")
'''

#wap to check given no is harshad no or not
#eg=18 1+8=9 and 18 is divisible by 9 . egs are 12,21
'''
n=int(input())
sum=0
dummy=n
while dummy>0:
    rem=dummy%10
    dummy//=10
    sum+=rem
if n%sum==0:
    print("harshad no")
else:
    print("not harshad no")
'''
#wap to print all disarium no from 1 to 100
'''
i=1
c=0
while i<1000:
    x=i
    sum=0
    a=len(str(x))
    
    while x>0:
        rem=x%10
        x//=10
        sum+=rem**a
        a-=1
    if sum==i:
        c+=1
        print(i)
    else:
        pass
    i+=1
print(c)
'''
#wap to print all amstrong no between a given range
'''
n=int(input())
m=int(input())
while n<m+1:
    x=n
    sum=0
    a=len(str(n))
    while x>0:
        rem=x%10
        x//=10
        sum+=rem**a
    if sum==n:
        print(n)
    n+=1

'''


        
#wap to print whether a no is prime or not
'''
n=int(input())
if n<=1:
    print("not a prime no")
else:
    for i in range(2,n//2+1):
        if n%i==0:
            print("not a prime no")
            break
    else:
        print("yes prime no")
'''
#using while loop 
'''
n=int(input())
if n>1:
    i=2
    while i<n//2+1:
        if n%i==0:
            print("not a prime no")
            break
        i+=1
    else:
        print("Prime no")
'''      
#wap to print all prime no between 1 to 100
'''
i=1
while i<101:
    if i>1:
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            print(i)
    else:
        pass
    i+=1

'''
#write a prg to reverse a given string without using slicing
'''
n=input()
reverse=""
for i in n:
    reverse=i+reverse
print(reverse)  
'''
'''
n=input()
rev=""
for ip in range(-1,-(len(n)+1),-1):
    rev+=n[ip]
print(rev)

'''
#waptp every third prime no in  a given range 
'''
n=int(input())
m=int(input())
l=[]
for i in range(n,m+1):
    if i>1:
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            l.append(i)
    else:
        pass
print(l)
print(l[2::3])
'''

#waptp every second armstrong no in a givwn range
'''
n=int(input())
m=int(input())
l=[]
while n<m+1:
    x=n
    sum=0
    a=len(str(n))
    while x>0:
        rem=x%10
        x//=10
        sum+=rem**a
    if sum==n:
        l.append(n)
    n+=1
print(l)
print(l[1::2])
'''
#waptp harshad no in a given range
'''
n=int(input())
m=int(input())
while n<m+1:
    x=n
    sum=0
    while x>0:
        rem=x%10
        x//=10
        sum+=rem
    if n%sum==0:
        print(n)
    n+=1
'''
#waptp every second harshad no in a given range
'''
n=int(input())
m=int(input())
c=0
while n<m+1:
    x=n
    sum=0
    while x>0:
        rem=x%10
        x//=10
        sum+=rem
    if n%sum==0:
        c+=1
        if c%2==0:
            print(n)
    n+=1
'''
#or
'''
n=int(input())
m=int(input())
l=[]
while n<m+1:
    x=n
    sum=0
    while x>0:
        rem=x%10
        x//=10
        sum+=rem
    if n%sum==0:
        l.append(n)
    n+=1
print(l[1::2])

'''

#waptp all disarium no in a given range
'''
n=int(input())
m=int(input())
while n<m+1:
    x=n
    sum=0
    a=len(str(n))
    while x>0:
        rem=x%10
        x//=10
        sum+=rem**a
        a-=1
    if sum==n:
        print(n)
    n+=1
'''
#waptp every second disarium no in a given range
'''
n=int(input())
m=int(input())
c=0
while n<m+1:
    x=n
    sum=0
    a=len(str(n))
    while x>0:
        rem=x%10
        x//=10
        sum+=rem**a
        a-=1
    if sum==n:
        c+=1
        if c%2==0:
            print(n)
    n+=1
'''
#waptp perfect no in a given range
'''
n=int(input())
m=int(input())
for i in range(n,m+1):
    sum=0
    for j in range(1,i//2+1):
        if i%j==0:
            sum+=j
    if sum==i:
        print(i)
'''
'''
n=int(input())
m=int(input())
while n<m+1:
    sum=0
    i=1
    while i<n//2+1:
        if n%i==0:
            sum+=i
        i+=1
    if sum==n:
        print(n)           
    n+=1

'''

    
#waptp every second perfect no in a given range

'''
n=int(input())
m=int(input())
l=[]
for i in range(n,m+1):
    sum=0
    for j in range(1,i//2+1):
        if i%j==0:
            sum+=j
    if sum==i:
        l.append(i)
print(l)
print(l[1::2])
'''


















































































































































































