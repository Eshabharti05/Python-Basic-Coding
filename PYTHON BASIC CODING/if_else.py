'''
n=int(input())
if n%2!=0:
    print('odd number')
else:
    print('even number')
'''
'''
n=int(input('enter a no :'))  
n1=int(input('enter a no :'))
if n>n1:
    print(n,' is greater')
if n==n1:
bv    print('both are equal')
else:
    print(n1,' is greater')
'''

'''
s=input('enter a string : ')
if s==s[::-1]:
    print('yes it is palindrome')
else:
    print('no it is not a palindrome')
'''

#anagram
'''
s=input('enter 1st string: ')
s1=input('enter 2nd string: ')
if sorted(s)==sorted(s1):
    print("yes anagram")
else:
    print("no it's not anagram")
    
'''
#whether a person is eligible to vote or not
'''
s=int(input("enter your age : "))
if s>=18:
    print("yes eligible to vote")
else:
    print("not eligible to vote")
    
'''
#wheather a string has unique elements
'''
s=input("enter a string : ")
print(set(s))
if sorted(s)==sorted(set(s)):
    print("unique")
else:
    print("Duplicate")

'''
'''
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = list1 + list2
print(len(list3))

'''
'''
num_list = [4, 3, 2, 1]
sorted_list = sorted(num_list, reverse=True)
print(sorted_list[-1])

'''
'''
l1 = [1, 2, 3]
l2 = [3, 4, 5]
l3 = [i for i in l1 if i not in l2] + [i for i in l2 if i not in l1]
print(l3)

'''
#input="Hello, World"  output=10 . ignore all non alphabets
'''
def characters(string):
  count = 0
  for char in string:
      if char.isalpha():
          count += 1         
  return count
string = input()
result = characters(string)
print(result)

'''
#wap to display hello if a no entered by user is a multiple of five
#otherwise print bye
'''
num=int(input("enter a number: "))
if num%5==0:
  print("Hello")
else:
  print("Bye")

'''

#wap to cal electricity bill
'''
n=input("enter your unit")
if n<=100:
  print("Price : no charge")
if n>100 and n<=200:
  print()
if n
'''
#wap to display the last digit of the number
'''
num=int(input("enter a number : "))
a=num%10
print("Last digit of the number is " ,a)

'''
#wap to check whather the last digit of a number is divisible by 3 or not

'''
num=int(input("enter a number : "))
a=num%10
if a%3==0:
  print("Yes the last digit is divisible by 3")
else:
  print("No, he last digit is not divisible by 3")

'''
#wap to accept percentage from the user and display
'''
num=int(input("enter your percentage : "))
if num>90:
  print("Grade A")
if num>80 and num<=90:
  print("Grade B")
if num>=60 and num<=80:
  print("Grade C")
if num<60:
  print("Grade D")
'''
#wap to accept the cp of a bike and display the road tax to be paid
#costprice_with_taxes  >100000-15% , >50000 & <=100000-10% , <=50000-5%
'''
num=int(input("enter your cost price of bike : "))
tax=0
if num>100000:
  tax=num*0.15
elif num>50000 and num<=100000:
  tax=num*0.10
else:
  tax=num*0.05
print("tax to be paid ",tax)
'''
#wap to check whether a yr is leap yr or not

'''
yr=int(input("enter a year :"))
if (yr%4==0 and yr%100!=0) or (yr%400==0):
    print("leap year")
else:
    print("not a leap year")
'''

#wap to accept a no from 1 to 7 and display the name of the day like 1 for sunday,2 for monday and so on
'''
num=int(input("enter a number from 1 to 7 : "))
if num==1:
  print("Sunday")
elif num==2:
  print("Monday")
elif num==3:
  print("Tuesday")
elif num==4:
  print("Wednesday")
elif num==5:
  print("Thursday")
elif num==6:
  print("Friday")
elif num==7:
  print("Saturday")
else:
  print("enter a number from 1 to 7 ")
'''
'''
city=input("enter a city to see the monuments : ")
if city.lower()=="delhi":
  print("Red fort")
elif city.lower()=="agra":
  print("Taj Mahal")
elif city.lower()=="jaipur":
  print("Jai Mahal")
'''

#wap to check whether a number entered is three digit or not
'''
num=input("enter  a  number :")       #remember len function cannot be used on svdt that means int
if len(num)==3:
  print("it is a 3 digit number")
else:
  ("It is not a 3 digit number")
'''
#wap to display the middle digit of the 3 digit number
'''
num=int(input("enter  a  number : "))
a=num%100//10
if len(num)==3:
  print("Middle number is ",a)
'''
#wap to check whether a person is senior citizen or not
'''
age=int(input("enter  your age : "))
if age>=60:
  print("Senior citizen")
else:
  print("not a senior citizen")

'''
#wap to find the lowest no among two numbers
'''
n=int(input("enter  1st  number : "))
n1=int(input("enter  1st  number : "))
if n>n1:
  print(n," is greater")
elif n=n1:
  print("both are equal")
else:
  print(n1, " is greater") 
'''
#wap  to check whether a number is positive or negative
'''
n=int(input("enter  a  number : "))
if n>=0:
  print("Positive number")
elif n<0:
  print("Negative number")
  
'''  
#wap to check whether a number is divisible by 2 and 3 both
'''
n=int(input("enter  a  number : "))
if n%2==0 and n%3==0:
  print("it is divisible by 2 and 3 both")
elif n%3==0:
  print("it is not divisible by 2 and 3 both")
'''
#accept the temp in degree celsius of water and check whether it is boiling or not
'''
n=int(input("enter  your water temperature : "))
if n>=100:
  print("water is boiling")
else:
  print("it is not boiling")
'''
#accept the age of 4 people and display youngest one
'''
n=int(input("enter age of 1st person : "))
n1=int(input("enter age of 2nd person : "))
n2=int(input("enter  age of 3rd person : "))
n3=int(input("enter age of 4th person: "))
if n<n1 and n<n2 and n<n3 :
  print("1st person is the youngest")
elif n1<n and n1<n2 and n1<n3:
  print("2nd person is the youngest")
elif n2<n and n2<n1 and n2<n3:
  print("3rd person is the youngest")
elif n3<n and n3<n2 and n3<n1:
  print("4th person is the youngest")
'''


#wap to check whether a string startswith a vowel or not
'''
n=input("enter  a  string : ")
if n.startswith('a') or n.startswith('A') or n.startswith('e') or n.startswith('E') or n.startswith('I') or n.startswith('i') or n.startswith('O') or n.startswith('o') or  n.startswith('U') or n.startswith('u') :
  print("starts with vowel")
else:
  print("not starts with vowel")
'''

#wap to check a character is vowel or not
'''
n=input("enter  a  character : ")
vow="aeiouAEIOU"
if len(n)==1:
  if n in vow:
    print("vowel")
  else:
    print("not a vowel")
else:
  print("enter a charcter:")
'''

#wap to check if a no is positive negative or zero
'''
n=int(input())
if n==0:
    print("it is zero")
elif n<0:
    print("negative")
else:
    print("positive")
'''
#Create a program that calculates the discount on a purchase based on the total amount. If the total is greater than $100, apply a 10% discount; otherwise, apply a 5% discount.
# Write a program that takes a temperature in Celsius as input and converts it to Fahrenheit using the formula: F = (C * 9/5) + 32.
'''
c=int(input("enter temperature in celsius"))
f=(c*9/5)+32
print(f)
'''
#Build a Python program that calculates the BMI (Body Mass Index) of a person based on their weight
#(in kg) and height (in meters) and provides a classification (Underweight, Normal, Overweight, or Obese)
'''
n=float(input("enter your weight in kg :"))
n1=float(input("enter your height in meters :"))
bmi=float(n/(n1)**2)
print("Your bmi is ",bmi)
if bmi<18.5:
    print("underweight")
elif bmi>=18.5 and bmi<25:
    print("normal")
elif bmi>=25 and bmi<30:
    print("overweight")
else:
    print("obeise")
'''

#Develop a program that calculates the area of a triangle given its base and height.
'''
b=float(input("enter base of triangle :"))
h=float(input("enter height of triangle :"))
area=1/2*b*h
print("area of triangle ",area)
'''

# Implement a Python program that simulates a basic calculator. It should take two
#numbers and an operator (+, -, *, /) as input and perform the corresponding calculation.
'''
n=float(input("enter first number :"))
n1=float(input("enter second number :"))
o=input("enter an operator number :")
if o=='+':
    print(n+n1)
elif o=='-':
    print(n-n1)
elif o=='*':
    print(n*n1)
elif o=='/':
    print(n/n1)
elif o=='**':
    print(n**n1)
elif o=='//':
    print(n//n1)
else:
    print("enter correct operator")
'''

#accept total no of working days and
#total no of absent and calculate the
#percentage of class attendance
'''
n=int(input("total no of working days"))
s=int(input("total no of absent"))
attended_class=n-s
print(attended_class," total attended classes" )
percentage=(attended_class/n)*100
print("percentage of attended classes ",percentage)
if percentage<75:
    print("the student is not able to sit in exam")
else:
    print("allowed to sit in exam")
'''
#a company decided to give bonus to emp according to criteria
# timeofperiod-more than 10 yrs ,>=6 and <=10 ,less than 6 yrs
#bonus - 10%,8%,5%
'''
n=int(input("enter time period of service :"))
sal=int(input("enter your salary :"))
if n>10:
    bonus=sal*10/100
    print(bonus) 
elif n>=6 and n<=10:
    bonus=sal*8/100
    print(bonus)
else:
    bonus=sal*5/100
    print(bonus)
'''

'''
units=int(input())
if units<=100:
    print("no charge")
elif units<=200:
    print((units-100)*5)
else:
    print(500+(units-200)*10)
'''
 #wapto find the maxamong 3 numbers using nested if
'''
a=int(input())
b=int(input())
c=int(input())
if a>b:
    if a>c:
        print(a,"a max")
    else:
        print(c,"c max")
else:
    if b>c:
        print(b,"b max")
    else:
        print(c,"c max")
'''
#wapto find the maxamong 4 numbers using nested if
'''
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a>b:
    if a>c:
        if a>d:
            print(a,"a Max")
        else:
            print(d,"d max")
    else:
        if c>d:
            print(c,"c max")
        else:
            print(d,"d max")
else:
    if b>c:
        if b>d:
            print(b,"b max")
        else:
            print(d,"d max")
    else:
        if c>d:
            print(c,"c max")
        else:
            print(d,"d max")

'''
'''
i=3
j=5
k=7
if i<j:
    if j<k:
        i=j
    else:
        j=k
else:
    if j>k:
        j=i
    else:
        i=k
print(i,j,k)
'''
'''
n=int(input("enter your age"))
n2=input("enter your gender: M-Male and F=Female")
n1=int(input("no of days"))
if n>=18 and n<30:
    if n2=='M':
        print("Wage are ", 700*n1)
    else:
        print("Wages are",750*n1)
        
elif n>=30 and n<=40:
    if n2=='M':
        print("Wage are ",800*n1)
    else:
        print("Wage are", 850*n1)
    
'''    













