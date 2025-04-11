#for inside for-----LOOP--------------------------------------------
#breaking inner loop with outer loop value 

'''
for i in range(1,6):
    for j in range(1,6):
        print(i,j)
        if i==3:
            break
'''
'''
for i in range(1,6):
    for j in range(1,6):
        if i==3:
            break
        print(i,j)
'''

#breaking inner loop with inner loop value
'''
for i in range(1,6):
    for j in range(1,6):
        print(i,j)
        if j==3:
            break
        
'''
'''
for i in range(1,6):
    for j in range(1,6):
        if j==3:
            break
        print(i,j)
'''
#breaking outer loop with inner loop value
'''
for i in range(1,6):
    for j in range(1,6):
        print(i,j)
    if j==3:
        break
'''
'''
for i in range(1,6):
    for j in range(1,6):
        print(i,j)
    if j==5:
        break
'''
'''
for i in range(1,6):
    if j==5:
        break
    for j in range(1,6):
        print(i,j)
#op=error   
'''
#breaking outer loop with outer loop value
'''
for i in range(1,6):
    if i==3:
            break
    for j in range(1,6):
        print(i,j)
'''   

'''
for i in range(1,6):
    for j in range(1,6):
        print(i,j)
    if i==3:
        break
'''



#while inside while-----LOOP--------------------------------------------

#just eg of while inside while
'''
i=1
while i<6:
    j=1
    while j<6:
        print(i,j)
        j+=1
    i+=1
'''
#breaking inner loop with outer loop value
'''
i=1
while i<5:
    j=1
    while j<5:
        if j==1:
            break
        print(i,j)
        j+=1
    i+=1
'''
#breaking inner loop with outer loop vALUE
'''
i=1
while i<5:
    j=1
    while j<5:
        print(i,j)
        if i==3:
            break
        j+=1
    i+=1
'''
'''
i=1
while i<5:
    j=1
    while j<5:
        if i==3:
            break
        print(i,j)
        j+=1
    i+=1
'''

#breaking outer loop with outer loop vALUE
'''
i=1
while i<4:
    j=1
    while j<4:
        print(i,j)
        j+=1
    if i==3:
        break
    i+=1
'''
'''
i=1
while i<4:
    if i==2:
        break
    j=1
    while j<4:
        print(i,j)
        j+=1
    i+=1
'''
#breaking outer loop with inner loop vALUE
'''
i=1
while i<4:
    if j==2:
        break
    j=1
    while j<4:
        print(i,j)
        j+=1
    i+=1
'''

'''
i=1
while i<4:
    j=1
    if j==2:
        break
    while j<4:
        print(i,j)
        j+=1
    i+=1
'''
'''
i=1
while i<4:
    j=1
    while j<4:
        print(i,j)
        j+=1
    if j==2:
        break
    i+=1
'''































































































































