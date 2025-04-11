#for loop with list ,tuple,set,dictionary,string
'''
n=input("enter a string")
for i in n:
    print(i)

l=[22,33,44,"bye"]
for i in l:
    print(i)

d={"name":"esha","age":23}
for i in d:
    print(i)

d={"name":"esha","age":23}
for key,value in d.items():
    print(key,value)

d={"name":"esha","age":23}
for key in d:
    print(key,d[key])

s={11,33,44,"keelooo"}
for i in s:
    print(i)
'''
#how many elements are there in a given str (or)
#wap to show the implementation of len function
'''
n=input()
count=0
for i in n:
    count+=1
print(count)
'''
#wap to print how many times a given substr  is present in specified str
#(or) wap to show the implementation of count function
#note: only one element we can take as substr
'''
n=input("enter a string")
substr=input("enter a substr")
count=0
for i in n:
    if i==substr:
        count+=1
print(count)
'''
#how many vowels are present in a given str
'''
n=input()
count=0
for i in n:
    if i in 'aeiouAEIOU':
        count+=1
    else:
        pass
print("no of vowels",count)
'''
#WAP TO CHECK HOW MANY CONSONENTS ARE THER
'''
n=input()
count=0
for i in n:
    if i.isalpha():
        if i not in 'aeiouAEIOU':
            count+=1
print("no of consonents",count)
'''
#wap to check how many consonents and vowels are there
'''
n=input()
cons=0
vowels=0
for i in n:
    if i.isalpha():
        if i in 'aeiouAEIOU':
            vowels+=1
        elif i not in 'aeiouAEIOU':
            cons+=1
        else:
            pass
print("no of consonents",cons)

print("no of vowels",vowels)

'''
#wap to print how many digits are present in a given string
'''
n=input()
count=0
for i in n:
    if i.isdigit():
        count=count+1
print(count)
'''

#wap to print how many digits are there in a string without any repitations
'''
n=input()
count=0
for i in n:
    if i in '0123456789':
        count=count+1
print(count)
'''
'''steps to write this program:
1) take an input from user
2) assume that string contains 0 digits
3) iteration1: lets n=esha123
i='e' then
it will go to if block i is not in 0123456789 so out of if block
iteration 2: n=esha123
i='s' then
it will go to if block i is not in 0123456789 so out of if block
iteration 3: n=esha123
i='h' then
it will go to if block i is not in 0123456789 so out of if block
iteration 4: n=esha123
i='a' then
it will go to if block i is not in 0123456789 so out of if block
iteration 5: n=esha123
i='1' then
it will go to if block i is  in 0123456789 so (count=1)
iteration 6: n=esha123
i='2' then
it will go to if block i is  in 0123456789 so (count=2)
iteration 7: n=esha123
i='3' then
it will go to if block i is  in 0123456789 so (count=3)
4) then it will print count=3
'''
#wap to print even digits present in a given string.(without built-in methods)
'''
n=input()
for i in n:
    if i.isdigit():
        if i in '02468':
            print(i)
'''
'''
steps to write this program:
1) take an input from user
2) assume that string contains 0 digits
3) iteration1: lets n=esha123
i='e' then
it will go to if block i is not in 02468 so out of if block
iteration 2: n=esha123
i='s' then
it will go to if block i is not in 02468 so out of if block
iteration 3: n=esha123
i='h' then
it will go to if block i is not in 02468 so out of if block
iteration 4: n=esha123
i='a' then
it will go to if block i is not in 02468 so out of if block
iteration 5: n=esha123
i='1' then
it will go to if block i is  in 02468 so (count=0)
iteration 6: n=esha123
i='2' then
it will go to if block i is  in 02468 so (count=1)
iteration 7: n=esha123
i='3' then
it will go to if block i is  in 02468 so (count=1)
4) then it will print count=1
'''
#wap to print even digits present in a given string.(with built in method)
'''
n=input()
for i in n:
    if i.isdigit():
        if int(i)%2==0:
            print(i)

'''
'''
steps to write this program:
1) take an input
2)iteration1: lets n=esha123
i='e' then
it will go to if block i is not an integer so out of if block
iteration 2: n=esha123
i='s' then
it will go to if block it is not not an integer so out of if block
iteration 3: n=esha123
i='h' then
it will go to if block it is not an integer so out of if block
iteration 4: n=esha123
i='a' then
it will go to if block it is not an integer so out of if block
iteration 5: n=esha123
i='1' then
it will go to if block it is an integer and not divisible by 2 so (count=0)
iteration 6: n=esha123
i='2' then
it will go to if block it is  an integer and divisible by 2 so (count=0+1)
iteration 7: n=esha123
i='3' then
it will go to if block it is an integer and not divisible by 2 so (count=1+0)
4) then it will print count=1
'''

#wap to find sum of digits presents in a given string

'''
n=input()
count=0
for i in n:
    if i.isdigit():
        count=int(i)+count
print(count)
'''
'''
steps to write this program:
1) take an input
2) we will assume that integer sum is 0 if it is empty.
3)iteration1: lets n=esha123
i='e' then
it will go to if block i is not an integer so out of if block
iteration 2: n=esha123
i='s' then
it will go to if block it is not not an integer so out of if block
iteration 3: n=esha123
i='h' then
it will go to if block it is not an integer so out of if block
iteration 4: n=esha123
i='a' then
it will go to if block it is not an integer so out of if block
iteration 5: n=esha123
i='1' then
it will go to if block it is an integer and so (count=0+int(i))that means count=1
iteration 6: n=esha123
i='2' then
it will go to if block it is  an integer and (count=1+int(i)) that means count=1+2=3
iteration 7: n=esha123
i='3' then
it will go to if block it is an integer and (count=3+int(i))that means count=3+3=6
4) then it will print count=6
'''
#wap to print how many special characters are present in given string
'''
n=input()
count=0
for i in n:
    if  i.isalnum()==False:
        count=count+1
print(count)
'''
'''
steps to write this program:
1) take an input
2) assume that there is no special character in the string count=0
3) iteration1: lets take n="he ,@1"
i='h' then
it will go to if block it is alphabet so out of if block
iteration2: lets take n="he ,@1"
i='e' then
it will go to if block it is alphabet so out of if block
iteration3: lets take n="he ,@1"
i=' ' then
it will go to if block it is not alnum(that means it is not an integer as well as alphabet) so enter into if block
then count=0+1=1
iteration4: lets take n="he ,@1"
i=',' then
it will go to if block it is not alnum(that means it is not an integer as well as alphabet) so enter into if block
then count=1+1=2
iteration3: lets take n="he ,@1"
i='@' then
it will go to if block it is not alnum(that means it is not an integer as well as alphabet) so enter into if block
then count=2+1=3
iteration6: lets take n="he ,@1"
i='1' then
it will go to if block it is integer so out of if block
4)lastly it will print count=3

'''

#wap print the sum of numbers present in a given list
'''
l=eval(input("enter a list data "))
sum=0
for i in l:
    if type(i)==int:
        sum=sum+i
print(sum)

'''
'''
steps for writing this program
1)take an input in the form of list
2)assume that sum of all integers in that list is 0
3) iteration1:lets take l=[11,22,'heelo','2']
i=11 then it will go to if block
it will check the type of i . the type of i is int so sum=0+i (sum=0+11=11)
 iteration2:lets take l=[11,22,'heelo','2']
i=22 then it will go to if block
it will check the type of i . the type of i is int so sum=0+i (sum=11+22=33)
iteration3:lets take l=[11,22,'heelo','2']
i='heelo' then it will go to if block
it will check the type of i . the type of i is not int so out of if block
iteration4:lets take l=[11,22,'heelo','2']
i='2' then it will go to if block
it will check the type of i . the type of i is not int.it is string so out of if block
4)lastly print the total sum that is 33

'''
#wap to print frequency of each and every element
'''
n=input()
d={}
for i in n:
    if i in d:         # if i not in d:
        d[i]+=1     #      d[i]=1
    else:             # else:
        d[i]=1        #      d[i]+=1
print(d)
'''
'''
steps for writing this program:
1)take an string input
2) take an empty dictionary
3)iteration1: n=esshha
i='e' then it will enter if block i is not there so d[i]=1
( e:1 that means e has count:1.Since In dictionary d[key]=value is used for assigning new value to a dictionary)
iteration2: n=esshha
i='s' then it will enter if block i is not there so d[i]=1
( s:1 that means e has count:1.)
iteration3: n=esshha
i='s' then it will enter if block the condition is not satisfied
so it will enter else block i is already there in d so d[i]+=1 (that means s value will be updated from 1 to 2)
( s:2 that means e has count:2.)
iteration4: n=esshha
i='h' then it will enter if block i is not there so d[i]=1
( h:1 that means e has count:1.)
iteration5: n=esshha
i='h' then it will enter if block the condition is not satisfied
so it will enter else block i is already there in d so d[i]+=1 (that means h value will be updated from 1 to 2)
( h:2 that means e has count:2.)
iteration4: n=esshha
i='a' then it will enter if block i is not there so d[i]=1
( a:1 that means e has count:1.)
4)lastly it will print d.so output will be {'e':1,'s':2,'h':2,'a':1}
'''

'''
n=input()
d={}
for i in n:
    d[i]=n.count(i)
 #   print(n.count(i))
print(d)
'''
'''
steps for writing this prg:
1)take a string input
2)take an empty dictionary
3)iteration1:n=eess1
i='e' then d[i]=n.count(i) that means
(d[i] is used to assign new value to to i)
(n.count(i) means whatever element is in n string that will count the occurence of i)
so here 'e':2
iteration2:n=eess1
i='e' then d[i]=n.count(i) that means
(d[i] is used to assign new value to to i)
(n.count(i) means whatever element is in n string that will count the occurence of i)
so here 'e':2
iteration3:n=eess1
i='s' then d[i]=n.count(i) that means
(d[i] is used to assign new value to to i)
(n.count(i) means whatever element is in n string that will count the occurence of i)
so here 's':2
iteration4:n=eess1
i='e' then d[i]=n.count(i) that means
(d[i] is used to assign new value to to i)
(n.count(i) means whatever element is in n string that will count the occurence of i)
so here 's':2
iteration5:n=eess1
i='1' then d[i]=n.count(i) that means
(d[i] is used to assign new value to to i)
(n.count(i) means whatever element is in n string that will count the occurence of i)
so here '1':1
4) lastly it will print d.Since dictionary donot allow duplicates so output will be {'e':2,'s':2,'1':1}

'''
#range values

#-1 to -10(when we have negative updation add -1 to ending indexposition)
'''
for i in range(-1,-11,-1):
    print(i)
'''
#factorial of a given number
'''
n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
'''
'''
steps for writing this program:
1)take an integer input
2)factorial of 0 is 1.so assume fact=1
3)iteration1: n=3
Since there is range(1,4)  so i will iterate from 1 to 3(one less from endingvalue because updation is +1)
i=1 then fact=fact*i (that means fact=1*1=1)
iteration2: n=3
i=2 then fact=fact*i (that means fact=1*2=2)
iteration3: n=3
i=3 then fact=fact*i (that means fact=2*3=6)
then iteration completed
4)Lastly we have to print the fact value that is 6

'''


#wap to print the given no is perfect or no
#if the given no is equals too sum of the divisors of the given no (or ) factors of given no
#then it it called as perfect no eg-6 factors of 6=2,3,1(excluding number itself that is 6) and 3+2+1=6
'''
n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
#print(sum)
if n==sum:
    print("yes a perfect no")
else:
    print("not a perfect no")
'''
'''
steps for writing this program:
1)take an integer input
2) assuming the sum of all factors of given number be 0.
3)iteration1: n=6
Since there is range(1,5)  so i will iterate from 1 to 3(one less from endingvalue because updation is +1)
i=1 so it will enter if block 6 is divisible by 1 so (sum=0+i=0+1=1)
iteration2: n=6
i=2 so it will enter if block 6 is divisible by 2 so (sum=1+i=1+2=3)
iteration3: n=6
i=3 so it will enter if block 6 is divisible by 3 so (sum=3+i=3+3=6)
iteration4: n=6
i=4 so it will enter if block 6 is not divisible by 4  so sum remains same(sum=6)
iteration5: n=6
i=5 so it will enter if block 6 is not divisible by 5 so sum remains same(sum=6)
4) now , it will enter if block
n==sum that means (6==6) condition is true (as here we are getting sum as 6)
so it will print "yes a perfect no"
'''

#wap to print even no in a given range
'''
a=int(input())
n=int(input())
for i in range (a,n+1):
    if i%2==0:
        print(i)
'''
'''
ll=int(input())
ul=int(input())
for i in range (ll,ul+1,2):
    print(i)
'''
#for loop with range and cdt
'''
s="hello"
for index_pos in range(len(s)):
    print(index_pos,s[index_pos])
'''
#waptp the index postions of all the vowels present in a given string
'''
n=input()
for ip in range(len(n)):
    if n[ip] in 'AEIOUaeiou':
        print(ip)
'''
#wap to print elements which are present in even ip
'''
n=input()
for ip in range(0,len(n),2):
    print(n[ip])
'''
#wap to print sum of index_positions of the digits present in a given string
'''
n=input()
sum=0
for ip in range(len(n)):
    if n[ip].isdigit():
        sum+=ip
print(sum)
'''
#wap to add ip of even nos in a given string 
'''
n=input()
sum=0
for ip in range(len(n)):
    if ip in '02468':
        sum+=ip
print(sum)
'''
#wap to add ip of even nos in a given string 
'''
n=input()
sum=0
for ip in range(0,len(n),2):
    if n[ip] in '02468':
        sum=sum+int(n[ip])
print(sum)
'''
#wap find sum of odd ip of even digits
'''
n=input()
sum=0
for ip in range(len(n)):
    if ip%2!=0:
        if n[ip] in '02468':
            sum+=ip
print(sum)

'''   


#wap find sum of odd digits of odd ip
''' 
n=input()
sum=0
for ip in range(len(n)):
    if ip%2!=0 and n[ip] not in '02468':
        sum=sum+int(n[ip])
print(sum)
'''
#waptp the max no in agiven list and its index value
'''
l=[12,34,90,56,3]
max_val=l[0]
max_ip=0
for ip in range(1,len(l)):
    if l[ip]>max_val:
        max_val=l[ip]
        max_ip=ip
print(max_val,max_ip)
'''
#wap to print how many times given ssubstring is present in
#specified string
'''
ms=input()
ss=input()
c=0
for ip in range(len(ms)-len(ss)+1):
    if ms[ip:ip+len(ss)]==ss:
        c+=1
print(c)
'''
#ip=[11,22,33,44,55,66]
#op=[22, 11, 44, 33, 66, 55]
'''
n=[11,22,33,44,55,66]
for ip in range(0,len(n),2):
    if len(n)%2==0:
        n[ip],n[ip+1]=n[ip+1],n[ip]
print(n)
'''
#ip=[11,22,33,44,55,66]
#op=[66,55,44,33,22,11]

l=[11,22,33,44,55,66]
n=list()
print(right)
for ip in range(len(l)//2):
     l[ip]

print(n)
    

        
        
    





























