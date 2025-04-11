#how to create infinite loop ---- by while True

#taking multiple inputs
'''
l=[]
while True:
    value=int(input())
    if value<0:
        break
    l.append(value)
'''
#take 5 inputs from user and print even numbers

'''
l=[]
for i in range(5):
    num=int(input())
    l.append(num)

for num in l:
    if num%2==0:
        print(num)
'''


 
#take 5 inputs from user and find prime no
'''
l=[]
for i in range(5):
    num=int(input())
    l.append(num)
   
prime_numbers = []
for i in l:
    if i>1:
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            prime_numbers.append(i)
print(prime_numbers)

'''
#take 5 elements from user and print amstrong no
'''

l=[]
for i in range(5):
    num=int(input())
    l.append(num)
amsno=[]
for i in l:
    sum=0
    y=i
    a=len(str(y))
    while y>0:
        rem=y%10
        y//=10
sum+=rem**a
    if sum==i:
        amsno.append(i)
print(amsno)
'''

#take 5 inputs from user and print harshad no
'''
l=[]
for i in range(5):
    n=int(input())
    l.append(n)
harshadno=[]
for i in l:
    y=i
    sum=0
    while y>0:
        rem=y%10
        y//=10
        sum+=rem
    if i%sum==0:
        harshadno.append(i)
print(harshadno)
'''
#take 5 inputs from user and print perfect no
'''
l=[]
for i in range(5):
    n=int(input())
    l.append(n)
    
perfectno=[]

for i in l:
    sum=0
    j=1
    while j<i//2+1:
        if i%j==0:
            sum+=j
        j+=1
    if i==sum:
        perfectno.append(i)
print(perfectno)
'''





#waptp first 100 prime nos
'''
c=0
n=2
while c<=100:
    for i in range(2,n//2+1):
        if n%i==0:
            break
    else:
        print(n)
        c+=1

    n+=1
'''
'''
c=0
n=2
while True:
    for i in range(2,n//2+1):
        if n%i==0:
            break
    else:
        c+=1
        print(n)
        if c==101:
            break
    n+=1
'''





#waptp prime no between 1 to 100
#take first no as 2 because 1 is not a prime no
'''
i=2
while i<101:
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        print(i)
    i+=1
'''
#waptp 10th prime no
'''
c=0
n=2
while c<=10:
    for i in range(2,n//2+1):
        if n%i==0:
            break
    else:
        c+=1
        if c==10:
            print(n)
    n+=1
'''
'''
c=0
n=2
while True:
    for i in range(2,n//2+1):
        if n%i==0:
            break
    else:
        c+=1
        if c==10:
            print(n)
            break
    n+=1
'''
#waptp print special no or strong no
'''
n=int(input())
y=n
sum=0
while y>0:
    rem=y%10
    y//=10
    fact=1
    i=1
    while i<rem+1:
        fact*=i
        i+=1
    sum+=fact
if sum==n:
    print("special no")
else:
    print("not  a special no")
'''  
#waptp first 4 special nos
'''
n=1
c=0
while True:
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
        c+=1
        print(n)
        if c==4:
            break   
    n+=1

'''
'''
n=1
c=0
while c<=3:
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
        print(n)
        c+=1
    n+=1
'''




























































































































