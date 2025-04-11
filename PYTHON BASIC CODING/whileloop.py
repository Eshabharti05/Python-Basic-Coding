#wap to print first 10 natural numbers
'''
i=1
while i<11:
    print(i)
    i+=1
'''
#pp to print all the even nos within the given nos
'''
n=int(input())
i=0
while i<n+1:
    if i%2==0:
        print(i)
    i+=1
'''
#wap to print sum of all numbers from 1 to given no 
'''
n=int(input())
sum=0
i=1
while i<n+1:
    sum+=i
    i+=1
print(sum)
'''
#pp to cal the sum of all the odd nos within a given no
'''
n=int(input())
sum=0
i=1
while i<n+1:
     if i%2!=0:
         sum+=i
     i+=1
print(sum)
'''
#print multiplication table for a given no
'''
n=int(input())
i=1
while i<11:
    print(n," x",i," =",n*i)
    i+=1
'''
#pp to count the total no of digits in a no
'''
n=int(input())
ip=0
count=0
while ip<len(str(n)):
    count+=1
    ip+=1
print(count)

'''
#count no of odd and even nos from a given series
'''
n=int(input())
m=int(input())
odd=0
even=0
i=n
while i<m+1:
    if i%2==0:
        even+=1
    else:
        odd+=1
    i+=1
print("count of odd numbers are",odd)
print("count of even numbers are",even)

'''
#pp to display all nos within a given range except the prime nos
'''
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end + 1):
  is_prime = True
  if num <= 1:
    is_prime = False
  elif num <= 3:
    is_prime = True
  elif num % 2 == 0 or num % 3 == 0:
    is_prime = False
  else:
    i = 5
    while i * i <= num:
      if num % i == 0 or num % (i + 2) == 0:
        is_prime = False
        break
      i += 6

  if not is_prime:
    print(num)
'''
#wap to print given no is perfect no or not
'''
n=int(input())
sum=0
i=1
while i<n//2+1:
    if n%i==0:
        sum+=i
    i+=1
if n==sum:
    print("yes perfect no")
else:
    print("not a perfect no")

'''
#wap to print wheather a no is  prime or not
'''
n=int(input())
fact_count=0
i=1
while i<n+1:
    if n%i==0:
        fact_count+=1
    i+=1
if fact_count<3:
    print("yes prime no")
else:
    print("not a prime no")
'''
#factorial of a given no
'''
n=int(input())
fact=1
i=1
while i<n+1:
    fact*=i
    i+=1
print(fact)

'''

#o/p 25 to 10
'''
i=25
while i>9:
    print(i)
    i-=1
'''
#o/p -1 to -10
'''
i=-1
while i>-11:
    print(i)
    i-=1
'''
#o/p -110 to -90
'''
i=-110
while i<-89:
    print(i)
    i+=1
'''
#wap to print even no in a given range
'''
n=int(input())
m=int(input())
i=n
while i<m+1:
    if i%2==0:
        print(i)
    i+=1
'''
#waptp the ip of all the vowels in a given string
'''
n=input()
ip=0
while ip<len(n):
    if n[ip] in 'AEIOUaeiou':
        print(ip)
    ip+=1
'''
#waptp the elements which are present in even index postion
'''
n=input()
ip=0
while ip<len(n):
    if ip%2==0:
        print(n[ip])
    ip+=1
'''
#find the sum of ip of the digits present in a given sttring
'''
n=input()
sum=0
ip=0
while ip<len(n):
    if n[ip].isdigit():
        sum+=ip
    ip+=1
print(sum)
'''

#wap to add ip of even nos in a given str
'''
n=input()
ip=0
sum=0
while ip<len(n):
    if n[ip] in '02468':
        sum+=ip
    ip+=1
print(sum)
'''
#wap to find the sum of even digits present in even ip
'''
n=input()
ip=0 
sum=0
while ip<len(n):
    if ip%2==0:
        if n[ip] in '02468':
            sum+=int(n[ip])
    ip+=1
print(sum)
'''
#wap to find the sum of odd digits of odd ip
'''
n=input()
ip=0
sum=0
while ip<len(n):
    if ip%2!=0:
        if n[ip] not in '02468':
            sum+=int(n[ip])
    ip+=1
print(sum)
'''
#wap a program to count the freq of a given substring
'''
ms=input()
ss=input()
c=0
ip=0
while ip<(len(ms)-len(ss)+1):
    if ms[ip:ip+len(ss)]==ss:
        c+=1
    ip+=1
print(c)
'''
#wap to print max no in a given list and its ip
'''
l=[23,45,100,3]
mxno=l[0]
mip=0
ip=0
while ip<len(l):
    if l[ip]>mxno:
        mxno=l[ip]
        mip=ip
    ip+=1
print(mxno)
print(mip)
'''
#wap to print min no in a given list and its ip
'''
l=[23,3,21,90]
minno=l[0]
ip=0
mip=0
while ip<len(l):
    if l[ip]<minno:
        minno=l[ip]
        mip=ip
    ip+=1
print(mip,minno)
 '''       
#Reading input until a specific word is entered:
'''
word = ""
while word != "quit":
    word = input("Enter a word (type 'quit' to exit): ")
    print("You entered:", word)
'''


#wap to print multication of each digit in a given no
'''
n=int(input())
product=1
while n>0:
    rem=n%10
    n//=10
    product*=rem
print(product)
'''
#strong no(12 1!+2! should be equal to 12 eg=145)
'''
n=int(input())
sumoffact=0
dummy=n
while dummy>0:
    rem=dummy%10
    dummy//=10
    fact=1   #we are declaring fact=1inside because for every ele fact should start with 1
    for i in range(1,rem+1):
        fact*=i
    sumoffact+=fact
    
if sumoffact==n:
    print("yes strong number")
else:
    print("not a strong number")


'''    
    
#convert  integer into binary no #for eg 2 binary no is 10

n=int(input())
binary_str=""
while n>0:
  rem=n%2
  n//=2
  binary_str=str(rem)+binary_str
print(binary_str)
  
#convert binary no to integer no



  




    
#evil or odious(first convert the no into binary if the no of 1's is divisible by 2 then it is evil no)
#happy no(1 and 7 are happy nos . if no greater than 10 then take ex= 12=1**2+2**2=5 not a happy no . )
#palyprime
'''
n=int(input())
fact_count=0
dummy=n

for i in range(1,dummy+1):
    if dummy%i==0:
        fact_count+=1
is_prime=True
if fact_count<3:
    is_prime=True
else:
    is_prime=False
    
reversed_no=0
while dummy>0:
    rem=dummy%10
    reversed_no=(reversed_no * 10)+rem
    dummy//=10

is_palindrome=True
if reversed_no==n:
    is_palindrome=True
else:
    is_palindrome=False
if is_palindrome==True and is_prime==True:
    print("yes palyprime no")
else:
    print("not a palyprime no")
'''
#emirp(a should be prime and it should not be palindrome and the reversed no should be prime)
'''
num = int(input("Enter a number: "))

is_prime = True
for i in range(2, int(num**0.5) + 1):
  if num % i == 0:
    is_prime = False
    break

reversed_num = int(str(num)[::-1])
is_reversed_prime = True
for i in range(2, int(reversed_num**0.5) + 1):
  if reversed_num % i == 0:
    is_reversed_prime = False
    break

if is_prime and is_reversed_prime:
  print(num, "is an emirp number.")
else:
  print(num, "is not an emirp number.")
'''
#fibbonacci

#write a program to print a number in reverse order
'''
n=int(input())
rno=0
while n>0:
    rem=n%10
    n//=10
    rno=rno*10+rem
print(rno)
'''













