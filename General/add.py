def take_input():
    x = int(input(" enter first number:-"))
    y = int(input(" enter second number:-"))
    return x,y
def add():
    x,y = take_input()
    return x+y

def sub():
    x,y = take_input()
    return x-y
    
def multiply():
    x,y = take_input()

    return x*y

def divied():
    x,y = take_input()
    return x/y

k = int(input('''
Enter 
    10 to add.
    20 to subtraction 
    30 to multiply
    40 to dived
'''
    ))
if k == 10:
    print(add())
elif k == 20:
    print(sub())elif k == 30:
    print(multiply())
elif k== 40:
    print(divied())        
else:
    print("Wrong choice exiting the program")

