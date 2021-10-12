'''
 functions
-------------
 def function_name(parameters):
    """ doc_string"""

    statements - is a function
    function/method both are same
   
   def - define(syntax)

 function = ekta boro programme k 
    choto choto ongshe vhag korake 
    function bole.

'''

def welcome():
   """ This is a document string """
   print('Hello,Gulshan.Good Morning')

welcome()

print(welcome.__doc__)

 # parameter

def welcome1(name):
    """ This is a another document string """
    print(f'Hello {name} Good Morning')

 # without Parameter

welcome1('Gulshan')
welcome1('Tanny')
print(welcome1.__doc__)

 # dui ta parameter

def welcome2(name,msg):
    print(f'Hello {name} {msg}')

welcome2('Maruf','Good Evening')
welcome2('Halder','Good Morning')

def welcome3(name1,name2,name3,name4):
    print(f'Hello {name1}')
    print(f'Hello {name2}')
    print(f'Hello {name3}')
    print(f'Hello {name4}')

welcome3('Sazib','Gulshan','Arman','Maruf')

# Python Arbitrary Arguments

# ----------- Loop ---------------

 # * means List

def welcome4(*name):
    for x in name:
        print(f'Hello {x}')

# calling function

welcome4('Sazib','Gulshan','Arman','Maruf','Shuvo','Nazmul')  # tuple - collection type

def welcome5():
    return 'I am from welcome5'
# welcome5()
print(welcome5())

# anonymous functions are also lambda function

# syntax of lambda functions

# function name = lambda arguments: expression 

# def double(x): # x hocche argument
#     return x*2
# result=double(10)
# print(result)
# print(double(100))

duigun=lambda x:x*2
print(duigun(50))

# function with return value

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

# using arbitrary keyword arguments

def build_profile(first,last,**kwargs):
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in kwargs.items():
        profile[key]=value
    return profile
print(build_profile('Gulshan','Rahman',location='Dhaka',field='IT'))


import math  # math hocche module
print(math.pi)
