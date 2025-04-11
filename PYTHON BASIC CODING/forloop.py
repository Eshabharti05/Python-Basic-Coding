#for loop with tuple
'''
s=(11,2,3,'hello')
for j in s:
    print(j)
'''    
#for loop with dict
'''
d={'name':'esha','age':23}
for i in d:
    print(i)
'''
'''
n=int(input())
for i in range(1,n):
    if i%2==0:
        print(i)
   '''
'''
n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)
'''
'''
n=int(input())
sum=0
for i in range(1,n):
    if i%2!=0:
        sum+=i
    
print(sum)
'''
'''
n=int(input())
for i in range(1,11):
    print(n," x " ,i, " =",n*i)
'''
'''
n=input()
count=0
for i in n:
    count=1+count
print(count)
'''

#Python program to check if the given string is a palindrome.
'''
n=input()
count=""
for i in n:
    count=i+count
if n==count:
    print("yes palindrome")
else:
    print("not a palindrome")
print(count)
'''
#Python program that accepts a word from the user and reverses it.
'''
n=input()
count=""
for i in n[::-1]:
    count+=i
print(count)
'''
'''
n=input()
s=n[::-1]
print(s)
'''



#Python program to count the number of even and odd numbers from a series of numbers.
'''
n=eval(input())
count_even=0
count_odd=0
for i in n:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print("no of even numbers are ",count_even)
print("no of odd numbers are ",count_odd)
'''
# Function to check if a number is prime
'''
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Input from user
number = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")




'''
#Python program that accepts a string and calculates the number of digits and letters.
'''
n=input()
letter=0
digit=0
for i in n:
    if i.isalpha():
        letter+=1
    elif i.isdigit():
        digit+=1
    else:
        pass
print(letter)
print(digit)
'''
#Python program to check the validity of password input by users
'''not able to write this'''

#find the output
'''
i=2
for i in "1234":
    print( i*2)
    break
'''
#Write a Python program to display only those numbers from a list that satisfy the following conditions
'''
The number must be divisible by five
If the number is greater than 150, then skip it and move to the following number
If the number is greater than 500, then stop the loop
'''
'''
n=[12, 75, 150, 180, 145, 525, 50]
for i in n:
    if i>500:
        break
    elif i>150:
        continue
    elif i%5==0:
        print(i)
'''            
    
    
#Print list in reverse order using a loop
'''
l=[7,6,9,88,34]
print(l[::-1])
'''
'''
l=[7,6,9,88,34]
new_list=reversed(l)
for i in new_list:
    print(i)
'''

#pp to get the fibbonacci series between 0 to 50
#eg=0,1,1,2,3,5,8
'''
not able to solve'''

#wap to find out factorial of a number
'''
n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial of the given no is ",fact)
'''

#Write a program that counts the frequency of each element in a list using a for loop.
'''
l=[2,2,2,2,3,9,9,9,9,9,5,5,4,2,2,3,5,6,6,7]

d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
'''
'''
l=[2,2,2,2,3,9,9,9,9,9,5,5,4,2,2,3,5,6,6,7]
freq={}
for i in set(l):
    freq[i]=l.count(i)
print(freq)
'''
#Given a list numbers = [1, 2, 3, 1, 2, 4, 5], use a for loop to remove duplicates.
'''
a=[]
n=[1, 2, 3, 1, 2, 4, 5]
for i in set(n):
    a.append(i)
#a=set(n)
#print(list(a))

'''

#Given an integer n, write a program that finds the sum of its digits using a for loop.
'''
n=int(input())
count=0
for i in str(n):
    count=count+int(i)
print(count)    
'''
#alculate the factorial of a number:
'''
n= int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
'''
#Create a list of squares of numbers from 1 to 5:
'''
squares = [x**2 for x in range(1, 6)]
print(squares)
'''
'''
l=[]
for i in range(1,6):
    l.append(i**2)
print(l)
'''

#Create a list of even numbers from 2 to 10:
'''
l=[]
for i in range(2,11):
    if i%2==0:
        l.append(i)
print(l)
'''
#Handle the IndexError exception:
'''
l=[1,2,3]
try:
    for i in range(2):
        print(l[i])
except IndexError:
    print("index out of range:")
'''
'''
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a number.")
'''
#wap to print a list with their index value
'''
my_list = [35, 62, 93, 45, 50]
for index, value in enumerate(my_list):
    print(index, value)
'''
#armstrong number

n=int(input())
a=len(str(n))
sum=0
for i in str(n):
    sum+=int(i)**a
if n==sum:
    print("yes armstrong no")
else:
    print("not a armstrong no")




















































    
