
a = int(input('Enter value for a:'))
b = int(input('Enter value for b:'))
c = int(input('Enter value for c:'))
d = int(input('Enter value for d:'))

if a>b and a>c and a>d:
    print(f'{a} is largest number')
elif b>c and b>d:
    print(f'{b} is largest number')
elif c>d:
    print(f'{c} is largest number')
elif a==b and b==c and c==d:
    print('They are all equal')
else:
    print(f'{d} is largest number')