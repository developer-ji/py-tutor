# n = int(input("Enter number:-  ")) # 5
n = 6
num = 1 # num 1
# while n >= 1: #1 > = 1 ->true
#     num = num * n #num = 120
#     n = n - 1   #n = 0
# for i in range(1,n+1): 
#     num *= i
#     print(num)
# print(num)

# 5
# 1
# 2
# 6
# 24
# 120

# a = int(input("Enter number:- "))
# n = 1
# for i in range(1, a+1):
#     n= n*i
#     # print(n)
# print(n)


# num = int(input("enter number:-"))
# n = 1
# while num>=1:
#     n = n*num
#     num = num-1
#     # print(n)
# print(n)

def factorial(a):
    num = 1
    while a >= 1:
        num = num * a
        a = a - 1
    return num
a = 5
print(factorial(a))