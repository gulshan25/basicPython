'''
 For the prime nmber we need to divide the number
 2 - n-1. If the number is devided by any of this number
 than number is not a prime number

'''

num = int(input("Input the number you want to check: "))
for i in range(2, num): # we don't mention n-1 in range because range don't count the last number
	if num%i == 0:
		print(f'This number {num} is not a prime number')
		break
else:
	print(f'This number {num} is a prime number')