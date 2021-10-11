'''
dictionary
-------------
variable = {'key':value}

HW = 10 person info

'''

person1 = {'Id':1,'Name':'Arman','Phone':'01545465677'}


print(person1['Id'],end='\t')
print(person1['Name'],end='\t')
print(person1['Phone'])
print(person1['Id'],end='\n')
print(person1['Name'],end='\n')
print(person1['Phone'])
# print(f'stud ['Id','Name','Phone']')

person2=person1.copy()
print(person2)

# use a update method

person2.update({'Name':'Sujon Raaj Bongshi'})
person2.update({'Age':16})
print(person2)

# delete by key 

del person2['Age']
print(person2)

print(type(person2))
print(dir(person2))

person2.clear()
print(person2)

print(person1.items())
print(list(person1.items()))

print('Display only keys:')
print(person1.keys())

print('Display only values:')
print(person1.values())

for k in person1.keys() :
    print(k,end='\t')


for k in person1.values() :
    print(k,end='\t')