# Filename:function.py
#define function
def sayHello():
    print 'Hello World!'

#excute function 
sayHello()

def printMax(a,b):
    '''get max value'''
    if a > b:
        print a, 'is maximum'
    else:
        print b, 'is maximun'

printMax(2,6)

x = 3
y = 9
printMax(x, y)
print printMax.__doc__
