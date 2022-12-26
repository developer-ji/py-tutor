


def take_input():
    x = int(input("enter first number:-"))
    y = int(input("enter second number:-"))
    return x,y

def add():
    x,y = take_input()
    return x+y
def sub():
    x,y = take_input()
    return x-y
def multy():
    x,y = take_input()
    return x*y
def divide():
    x,y = take_input()
    return x/y
def module():
    x,y = take_input()
    return x%y

kl = input('''enter:-
add 
sub
multy 
divide
module:-'''
)

if kl == "add":
    print(add())
elif kl == "sub":
    print(sub())
elif kl == "multy":
    print(multy())
elif kl == "divide":
    print(divide())
elif kl == "module":
    print(module())
else:
    print("Wrong choice exiting the program")
   




