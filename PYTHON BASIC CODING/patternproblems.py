'''
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        print("*",end=' ')
    print()
'''
'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
n=int(input())
for row in range(1,n+1):
    print('* '*n)
'''

'''
*
  *
    *
      *
        *
'''
#print pattern as shown above
'''
n=5
for row in range(1,n+1):
    for col in range(1,n+1):
         if row == col:
            print("*", end="")
         else:
            print(" ", end="")
    print()
'''
#print diagonal where row+col==n+1
'''
n=5
for row in range(1,n+1):
    for col in range(1,n+1):
         if row+col==n+1:
            print("*", end="")
         else:
            print(" ", end="")
    print()
'''
#print pattern after merging above two
'''
n=5
for row in range(1,n+1):
    for col in range(1,n+1):
         if row == col:
            print("*", end="")
         else:
            print(" ", end="")
    print()
for row in range(1,n+1):
    for col in range(1,n+1):
         if row+col==n+1:
            print("*", end="")
         else:
            print(" ", end="")
    print()

'''
#print pattern as
'''
n=5
for row in range(1,n+1):
    for col in range(1,n+1):
        print("*",end="")
        if row==col:
            break

    print()
           
'''
#print pateern as
'''
n=5
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col>=n+1:
            print("*",end="")
        else:
            print(' ',end='')

    print()
'''
'''
n=5
for row in range(1,n+1):
    for col in range(1,n+1):
        if row<=col:
            print("*",end="")
        else:
            print(' ',end='')

    print()

'''
'''
n=5
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col<=n+1:
            print("*",end="")
        else:
            print(' ',end='')

    print()
'''


#generic method to solve pattern problems

'''
*
 *
  *
   *
    *
'''
#wap to print
'''
n=5
stars=1
spaces=0
for row in range(1,n+1):
    for sp in range(1,spaces+1):
       print(' ',end='')
    for st in range(1,stars+1):
        print('*',end='')
    print()
    spaces+=1
'''







'''
    *
   *
  *
 *
*
'''
#wap to print
'''
n=5
stars=1
spaces=n-1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
       print(' ',end='')
    for st in range(1,stars+1):
        print('*',end='')
    spaces-=1
    print()
    
'''





'''
*
**
***
****
*****
'''
#wap to print
'''
n=5
stars=1
for row in range(1,n+1):
    for st in range(1,stars+1):
        print('*',end='')
    print()
    stars+=1
'''








'''
    *
   **
  ***
 ****
*****
'''
#wap to print above pattern

'''
n=5
stars=1
spaces=n-1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
       print(' ',end='')
    for st in range(1,stars+1):
        print('*',end='')
    print()
    stars+=1
    spaces-=1
'''







'''
*****
 ****
  ***
   **
    *
'''
#wap to print above pattern
'''
n=5
stars=n
spaces=0
for row in range(1,n+1):
    for sp in range(1,spaces+1):
       print(' ',end='')
    for st in range(1,stars+1):
        print('*',end='')
    print()
    stars-=1
    spaces+=1
'''





'''
*****
**** 
***  
**   
*
'''
#wap to print above pattern
'''
n=5
stars=n
spaces=0
for row in range(1,n+1):
    for st in range(1,stars+1):
        print('*',end='')
    for sp in range(1,spaces+1):
       print(' ',end='')
    
    print()
    spaces+=1  
    stars-=1   
'''
'''
n=int(input())
stars=n
for i in range(1,n+1):
    for st in range(1,stars+1):
        print('*',end='')
    print()
    stars-=1
'''


'''
    *  
   *  *  
  *  *  *  
 *  *  *  *  
*  *  *  *  *
'''
'''
n=int(input())
stars=1
for rows in range(1,n+1):
    for j in range(n-rows):
        print(' ',end='')
    for stars in range(1,rows+1):
        print('* ',end='')
   
    print()
'''


'''
    *  
   *  *  
  *  *  *  
 *  *  *  *  
*  *  *  *  *
'''
'''
n=int(input())
star=1
space=n-1
for row in range(1,n+1):
    for st in range(1,space+1):
        print(' ',end='')
    for st in range(1,star+1):
        print('* ',end='')
    print()
    star+=1
    space-=1
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
star=n
space=0
for row in range(1,n+1):
    for st in range(1,space+1):
        print(' ',end='')
    for st in range(1,star+1):
        print('* ',end='')
    print()
    star-=1
    space+=1
'''
'''
* * * * * 
 * * * * * 
  * * * * * 
   * * * * * 
    * * * * *
'''
'''
n=int(input())
star=n
space=0
for row in range(1,n+1):
    for st in range(1,space+1):
        print(' ',end='')
    for st in range(1,star+1):
        print('* ',end='')
    print()
    
    space+=1
'''



'''
    1
   12
  123
 1234
12345
'''
'''
n=5
spaces=n-1
stars=1
for row in range(1,n+1):
    dummy=1
    for sp in range(1,spaces+1):
        print(' ',end='')
    for st in range(1,stars+1):
        print(dummy,end='')
        dummy+=1

    print()
    spaces-=1
    stars+=1
'''




'''
        1
      12
    123
  1234
12345
'''
'''
n=5
spaces=n-1
stars=1
for row in range(1,n+1):
    dummy=1
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end='')
        dummy+=1

    print()
    spaces-=1
    stars+=1
'''    
'''
        1
      212
    32123
  4321234
543212345
'''
'''
n=5
spaces=n-1
stars=1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end='')
        if st<=stars//2:
            dummy-=1
        else:
            dummy+=1
        

    print()
    spaces-=1
    stars+=2
'''
'''
1
22
333
4444
55555
'''
'''
n=5
for row in range(1,n+1):
    for col in range(1,row+1):
        print(row,end='')
    print()
'''
'''
55555
4444
333
22
1
'''
'''
n=5
for row in range(n,0,-1):
    for col in range(row):
        print(row,end='')
    print()
'''
'''
55555
54444
54333
54322
54321
'''
'''
n=5
stars=5
for rows in range(1,n+1):
    dummy=n
    for col in range(1,n+1):
        print(dummy,end='')
        if  rows > col:
            dummy-=1
    print()

'''
'''
5
45
345
2345
12345
'''
'''
n=5
for row in range(n,0,-1):
    for col in range(row,n+1):
        print(row,end='')
    print()
'''
'''
12345
2345
345
45
5
'''
'''
n=5
for row in range(1,n+1):
    for col in range(row,n+1):
        print(col,end='')
    print()
'''
'''
54444
55444
55544
55554
55555
'''
'''
n=5
stars=5
for rows in range(1,n+1):
    dummy=n
    for col in range(1,n+1):
        print(dummy,end='')
        if  rows==col:
            dummy-=1
    print()
'''

#column wise incrementation
'''
12345
12345
12345
12345
12345
'''
'''
n=5
for row in range(1,n+1):
    dummy=1
    for col in range(1,n+1):
        print(dummy,end='')
        dummy+=1
    print()
'''
#row wise incrementation
'''
11111
22222
33333
44444
55555
'''
'''

n=5
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        print(dummy,end='')

    print()
    dummy+=1
'''
'''
12345
678910
1112131415
1617181920
2122232425
'''
'''
n=5
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        print(dummy,end='')
        dummy+=1
    print()
'''
'''
12345
23456
34567
45678
56789
'''
'''
n=5
dummy=1
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(dummy,end='')
        dummy+=1
    print()
'''
'''
16111621
27121722
38131823
49141924
510152025
'''
'''
n=5
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(dummy,end='')
        dummy+=5
    print()
'''
'''
12345
246810
34567
4681012
56789
'''
'''
n=5
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(dummy,end='')
        if row%2==0:
            dummy+=2
        else:
            dummy+=1
    print()
'''
'''
1
12
123
1234
12345
'''
'''
n=5
for row in range(1,n+1):
    dummy=1
    for col in range(row):
        print(dummy,end='')
        dummy+=1
    print()
'''
'''
1
22
333
4444
55555
'''
'''
n=5
dummy=1
for row in range(1,n+1):
    for col in range(row):
        print(dummy,end='')
    dummy+=1
    print()
'''
'''
55555
4444
333
22
1
'''
'''
n=5
dummy=n
for row in range(n,0,-1):
    for col in range(row):
        print(dummy,end='')
    dummy-=1

    print()
'''
'''
12345
1234
123
12
1
'''
'''
        
n=5
for row in range(n,0,-1):
    dummy=1
    for col in range(row):
        print(dummy,end='')
        dummy+=1
    print()
'''      
'''
54321
5432
543
54
5
'''
'''
n=5
for row in range(n,0,-1):
    dummy=n
    for col in range(row):
        print(dummy,end='')
        dummy-=1
    print()
'''
'''
5
45
345
2345
12345
'''
'''
n=5
for row in range(1,n+1):
    dummy=n
    for col in range(row):
        print(dummy,end='')
        dummy-=1

    print()
'''

'''
1
21
321
4321
54321
'''

'''
n=5
for row in range(1,n+1):
    dummy=n-row+1
    for col in range(row):
        print(dummy,end='')
        dummy+=1 
    print()
'''
'''
1
21
321
4321
54321
'''
'''
n=5
for row in range(1,n+1):
    dummy=row
    for col in range(row):
        print(dummy,end='')
        dummy-=1 
    print()
'''
'''
12345
2345
345
45
5
'''
'''
n=5
for row in range(n,0,-1):
    dummy=(n+1)-row
    for col in range(row):
        print(dummy,end='')
        dummy+=1 
    print()
'''
'''
1       1 
  2   2   
    3     
  4   4   
5       5
'''
'''

n=5
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==col or row+col==n+1:
            print(dummy,end=' ')
        else:
            print(' ',end=' ')
    print()
    dummy+=1
'''
'''
   1
 123
12345
'''
'''
n=int(input())
for row in range(1,n+1):
    spaces=n-row
    for sp in range(1,spaces+1):
        print(' ',end='')
    stars=1
    for st in range(1,2*row):
        print(stars,end=' ')
        stars+=1
    print()
'''
'''
        5
      54
    543
  5432
54321
'''
'''
n = 5
for i in range(1, n+1):
    for j in range(n-i, 0, -1):
        print(" ", end="")
    dummy=n
    for k in range(i, 0, -1):
        print(dummy, end="")
        dummy-=1
    print()
'''
'''
    1
   21
  321
 4321
54321
'''
'''
n = 5
for row in range(1, n+1):
    for j in range(n-row, 0, -1):
        print(" ", end="")
    for k in range(row, 0, -1):
        print(k, end="")
    print()

'''
'''
1234567
  12345
    123
      1

'''
'''
n=4
stars=2*n-1
spaces=0
for i in range(1,n+1):
    dummy=1
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end='')
        dummy+=1
    print()
    spaces+=1
    stars-=2
'''

'''
1     
  2   
    3 
  4   
5
'''
'''
n=5
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        if col<=n//2+1:
            if row==col or row+col==n+1:
                print(dummy,end=' ')
            else:
                print(' ',end=' ')
    print()
    dummy+=1
'''
'''
1       
  2     
    3   
      4 
    5   
  6     
7
'''
'''
n=7
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        if col<=n//2+1:
            if row==col or row+col==n+1:
                print(dummy,end=' ')
            else:
                print(' ',end=' ')
    print()
    dummy+=1
'''
'''
7654321
  654321
    54321
      4321
        321
          21
            1
'''
'''
n=int(input())
spaces=0
stars=n
for row in range(n,0,-1):
    dummy=row
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end='')
        dummy-=1
    print()
    stars-=1
    spaces+=1
'''









n=5
dummy=1
for row in range(n):
    for col in range(n):
        print(dummy,end='')
    print()
    dummy+=1


n=5
dummy=1
for row in range(n):
    for col in range(row):
        print(dummy,end='')
    print()
    dummy+=1








































































































































































