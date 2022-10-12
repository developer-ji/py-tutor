# # print('Q1:-')
# # n1 = int(input("enter number:-"))
# # for i in range(n1 ):

# #     print( i*"* ")  

# # print('Q2:-')
# # n2 = int(input("enter number:-"))
# # for i in range(n2,0,-1):
# #     print(i*"* ")


# # print("Q3:-")
# # user = int(input("enter number:-"))
# # for i in range(user):
# #     print(user*"* ")

# # print("Q4:-")
# # n4 = int(input("enter number:-"))
# # for i in range(0 , n4 ):
# #     print( ""* (n4- i) + "*" * i)

# # print("Q5:-")
# # n5 = int(input("enter number:-"))
# # for i in range(0 , n5 ):
# #     print( " " * (n5- i) + "*" * i )



# # print("Q6:-")
# n6 = 5
# for i in range(1,n6+1): # i =0
#   x = " "+" "*(n6- i) + "* " *i
#   print(x[:-1])
#   # print(" "+" "*(n6- i) + "* " *i) #       

# # for i in range(5):
# #   print(i*" *  ")


# # # print("hello1")
# # # print("hello2",end=" ")

# # # print("hello3")
# # #   *
# # #  **
# # # ***
# # n= 3
# # # for i in range(1,n+1):
# # #   print((n-i)*"_", end="")
# # #   print(i*"*")
# # for i in range(1,n+1):
# #   for j in range(n-i):
# #     print(" ", end="")
# #   print(i*"*")


 
# n = 5
# for i in range(1,n+1):#1, 2, 3, 4, 5
#   print((i-1)*" ",end="")
#   print((n-i+1)*"* ")

n = 15
# for i in range(1,n+1):#1, 2, 3, 4, 5
#   print((i-1)*" ",end="")
#   print((n)*"* ")

# user = int(input("enter number:-"))
# for i in range(1, user+1):
#   puserrint(*"*")

# *****
# ****
# ***   
# **
# *

'''
* * * * * *
* * * * *
* * * *
* * *
* *
*
'''
# print("* "*n)
# for i in range(1,n-2+1):
#   print("* ",end="")
#   print("  "*(i-1),end="")
#   print("* ",end="")
#   print("  "*(n -2*i-2),end="")
#   print("* ")
# print("* "*n)

# Get Chars appearing more than once
# xlr = "anantnag"
# x  = []
# y =[]
# for i in xlr:
#     if i not in x:
#         x.append(i)
#     elif i not in y:
#         y.append(i)
# print(y)

# Count occrance of 
xlr = input("Enter word:- ")  # amarkantak
usr = input("Enter character:- ") # 'k'
count = 0
for i in xlr:
    if i == usr:
        count = count+1
print(count)


def xl(ch):
    x = 0
    for i in xlr:
        if i ==  ch:
            x = x + 1
    return x
xl(usr)

