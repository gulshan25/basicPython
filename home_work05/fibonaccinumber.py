def fi_numbers(*number):
    for n in number:
        print(f'Fibonacci Number: {n} ')

fi_numbers('0','1','1','2','3','5','8','13','21','34')













# def add(x,y):
#     return x+y
#     print(fibonacci_number(1,2))


# fibonumber = lambda x:x+3
# print(fibonumber(5))

# fibonumber = lambda x:x+5
# print(fibonumber(8))


# x,y = 0,1
# print(x)
# while y<10:
#     print(y)
#     x,y = y, x+y



# num = int(input("Enter the number: "))
#  y = 0
#  x = 1
#  print(x)
#  while y<50:
#      print(y)
#      x = 1
#      y = 0+1

# n = int(input())
# print("Fibonacci series:", end = ' ')
# for n in range(0, n):  
#    print(fibonacciSeries(n), end = ' ')



# fi_Numbers = [0,1]

# if num >= 2:
#     for x in range(2, num):
#         x = fi_Numbers[num+1] + fi_Numbers[num-1]
#         fi_Numbers.append(x)
# print(fi_Numbers)

# f = int(input("Enter the value of 'f': "))

# x = 0
# y = 1
# num = 0
# count = 1

# while(count <=f):
#     count+=1
#     x=y
#     y=num
#     num = x+y
# print(sum,end="\t")


# f = int(input("Enter the fibonacci Number: "))

# for x in range(1,f+1):
#     print(x,end="\t")