
#sum of individual digits in a no 
'''
def sum(n):
    if n==0:
        return 0
    return n%10+sum(n//10)
print(sum(123))
'''
#print sum of first natural nos
'''
def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)
print(sum(5))
'''
#factorial of a given no
'''
def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)
print(factorial(5))
'''
#[11,[22,[33,10,20],100],90].waptp the sum of the digits of a nested list
'''
l=[1,[2,[3,10,2],1],9]
def sld(l):
    sum=0
    for i in l:
        if type(i)==list:
            sum+=sld(i)
        else:
            sum+=i
    return sum
print(sld(l))
'''
    
#[11,[22,[33,10,20],100],90].make it into a single list

'''
l=[1,[2,[3,10,2],1],9]
def flat(l):
    fl=[]
    for i in l:
        if type(i)==list:
            fl.extend(flat(i))
        else:
            fl.append(i)
    return fl
print(flat(l))
''' 


























































































































































    
