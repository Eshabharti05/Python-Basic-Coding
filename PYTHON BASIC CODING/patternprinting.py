'''
*
***
*****
'''
'''
n=int(input())
stars=1
for row in range(1,n+1):
    for st in range(1,stars+1):
        print('*',end='')
    stars+=2
    print()
'''
'''
    * 
   * * 
  * * * 
 * * * * 
* * * * *
'''
'''
n=int(input())
spaces=n-1
stars=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end='')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars+=1
    spaces-=1
'''
'''
* * * * * 
 * * * * 
  * * * 
   * * 
    *
'''
'''
n=int(input())
stars=n
spaces=0
for i in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end='')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces+=1
    stars-=1
'''
'''
n=int(input())
for row in range(n,0,-1):
    for sp in range(0,n-row):
        print(' ',end='')
    for st in range(row):
        print('*',end=' ')
    print()
'''


'''
    * 
   * * 
  * * * 
 * * * * 
* * * * *  
 * * * * 
  * * * 
   * * 
    *
'''
'''
n=int(input())
stars=1
spaces=n//2
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end='')
    for st in range(1,stars+1):
        print('*',end=' ')
    if row<=n//2:
        spaces-=1
        stars+=1
    else:
        spaces+=1
        stars-=1
    print()
'''
'''
****
***
**
*
'''
'''
n=int(input())
for row in range(n,0,-1):
    for col in range(row):
        print('*',end='')
    print()
'''
'''
*    
   
* *  
*  * 
*****
'''

'''
n=int(input())
for row in range(0,n):
    for col in range(0,n):
        if col==0 or row==n-1 or row==col:
            print('*',end='')
        else:
            print(end=' ')
    print()
'''
'''
*****
 *  *
  * *
   
    *
'''
'''

n=int(input())
for row in range(0,n):
    for col in range(0,n):
        if row==0 or col==n-1 or row==col:
            print('*',end='')
        else:
            print(end=' ')
    print()
'''
'''
   *   
  * *  
 *   * 
* * * *
'''
'''

n=int(input())
k=2
for row in range(1,n+1):
    for col in range(1,2*n):
        if row+col==n+1 or col-row==n-1:
            print('*',end='')
        elif row==n and col!=k:
            print('*',end='')
            k+=2
        else:
            print(end=' ')
    print()
'''
'''
 *** 
*   *
*   *
*****
*   *
*   *
*   *
'''
'''

for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=0) or ((row==0 or row ==3) and (col>0 and col<4)):
            print('*',end='')
        else: 
            print(end=' ')
    print()
        
'''
'''

*****
*    *
*    *
*    *
*****
'''
'''
n=int(input())
for row in range(n):
    for col in range(n):
        if (col==0 or col==n-1) or (row==0 or row==n-1):
            print('* ',end='')
        else:
            print(end='  ')


    print()
'''



        
'''
*   *
*   *
*   *
*   *
*   *
*   *
 *** 
'''
'''
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and (row!=6)) or (row==6 and (col>0 and col<4)):
            print('*',end='')
        else:
            print(end=' ')
    print()
'''
'''
*     *
 *   * 
  * *  
   *   
  * *  
 *   * 
*     *
'''
'''
for row in range(7):
    for col in range(7):
        if row==col or row+col==6:
            print('*',end='')
        else:
            print(end=' ')
    print()
'''
'''
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * *
'''
'''
n=int(input())
spaces=n-1
stars=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        if st%2==0:
            print('*',end=' ')
        else:
            print(' ',end=' ;)
    print()
    
    stars+=2
    spaces-=1
    
'''
'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''
'''
rows = 5
for i in range( rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
'''




























































































































































































































































































































































































































