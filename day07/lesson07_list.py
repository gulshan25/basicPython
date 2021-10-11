'''
list - collection of Data
-------------------------
listvar=[]

'''

motorcycles = ['Honda','Yamaha','Suzuki']
print(motorcycles)
# print(motorcycles[0])
# print(motorcycles[1])
# print(motorcycles[2])

'''
 for loop

'''

for moto in motorcycles:
    print(moto)

'''
for each - javascript

'''

i = 0
while i<2:
    print(motorcycles[i])
    i+=1  # compound assignment operator

'''
change
------

'''
# edit

motorcycles[1]='hero'
print(motorcycles)

# add - list -er last a

motorcycles.append('bajaj')
motorcycles.insert(2,'yamaha')
print(motorcycles)

fruits=[]
fruits.append('Mango')
fruits.append('Orange')
fruits.insert(2,'Jakefruit')
fruits.append('Banana')
fruits.append('Grape')
fruits.append('Lichi')
fruits.extend(['mango','bangi','watermelon','Dragonfruit','Grape','Apple'])

print(fruits)

# delete using index 

del fruits[7]
print(fruits)

# delete using item name 

fruits.remove('Grape')
fruits.remove('mango')
print(fruits)

fruits.pop()  # LIFO - last in first out
fruits.pop()  # LIFO - last in first out
print(fruits)
print(dir(fruits))

print(fruits.count('Mango'))
print(fruits.index('Mango'))
print(fruits.index('Lichi'))

fruits.reverse()
fruits.sort()  # ascending
fruits.sort(reverse=True)  # descending
print(fruits)

print(f'total number of fruits:{len(fruits)}')

# slicing list - 0 theke na 1 theke suru hoi 

# print(fruits[-1])
# print(fruits[-2])
# print(fruits[-3])
# print(fruits[0:3])
# print(fruits[2:5])
# print(fruits[3:])
# print(fruits[:4])
print(fruits[1:4:3])


# prime number h.w
