
#some example
'''
a=10
def fun():
    a=5
    print(a)
    a-=5
    print(a)
fun()
print(a)
'''
#exple of execution of nested functions
'''
def outer():
    print("outer started")
    def inner():
        print("inner started")
        print("inner ended")
    inner()
    print("outer ended")
outer()
 '''
'''
def outer():
    print("outer started")
    def inner():
        print("inner started")
        print("inner ended")
    print("outer ended")
outer()
inner()
'''

def outer():
    a=10
    def inner():
        print(a)
        a-=5
        print(a)
    inner()
outer()


























