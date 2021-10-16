'''
class - A class is a blueprint for the object
An object has 2 characteristics
a. Attributes
b. Behavior 
class className(object):
    --snip--

making an instances/object from a class
objectName=ClassName(arguments)
self - ei class-er method
'''

class calculator(object):
   def addition(self,x,y):
       return x+y

c1 = calculator() 
c1.addition(20,30)
print(c1.addition(20,30))
print(c1.subtraction(20,30))
print(c1.multiplication(20,30))
print(c1.division(20,30))


def add(x,y):
    return x+y
    print(add(10,3))

def sub(x,y):
    return x-y
    print(sub(10,3))

def mul(x,y):
    return x*y
    print(sub(10,3))

def div(x,y):
    return x/y
    print(div(10,3))