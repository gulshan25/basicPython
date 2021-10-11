'''
tuple 
-------

'''
magicians=('Sajib','Sujon','Sabyassachi','Sayeda')
print(magicians)

for m in magicians :
    print(m)

digits =(12,10,34,67,25,20,15,13,16,65)
print(digits)

print(max(digits))
print(min(digits))
print(sum(digits)) # jogfol

players= ('Arman','Arina','Maruf','Gulshan','Shuvo')
print(players[0:3])
print(players[0:0])

actors=players[:]
print(actors)

print(dir(actors))

print(actors.index('Gulshan'))
print(actors.count('Gulshan'))