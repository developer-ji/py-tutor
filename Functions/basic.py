# no of arguments bilkul barabar hona chahiye
# yahan par ek chahiye to ek hi pass krna padega na jyada na kam
# def xl(y):
#     return
# xl(6)

# postional argument
# def xl(x, y):
#     print(y) # 7
# xl(6,7)

# named argument
# Rule : Type Error if positional arg is repetead as named arg
# Rule : nam ed arg ke badd postional arg nhi kr skte
# def xl(x, y):
#     print(y) # 7
# xl(x=6,y=7) # named args
# xl(6,7) # postional  args
# xl(6,y=7) # postional args followed by named args
# xl(x=6,y) # named args followed by postional args and it is an error

# *args  we need to put aterik(*) sign
# we can pass any number of postional arguments  
# def xl(*args):
#     print(args[1]) # 7 args will be a tuple
# xl(6, 6)


# def xl(x, y, *args):
#     print(args[1]) 
# xl(6,{'a':4}, 6)

# def xl(x, y, *args): *args yanha par bta rha h wo kitne bhi positional arguments le skta h
#     print(args[1]) 
# xl(6,y=7)

# def xl(x, y, *args): #*args yanha par bta rha h wo kitne bhi positional arguments le skta h
#     print(args[1]) 
# xl(*range(9,20))


# def xl(a,b,c,d,e):
#     print(e) 
# xl(*[1,2,3,4,5])


# def xl(a,b,c,d,e, *args):
#     print(args)
# xl(5, *[4], **{"d":4,"e":5, "c":5, })

# def xl(a,b,c,d,e, *args,**kwargs):
#     print(kwargs)
# xl(5,6,7,8, *[4,],**{"z":4,"eq":5, "k":5, "f":8})
# jo function accept kare # number of arg or kwargs 
# jo hum pass kr skte h # positional followed by--> named


# x = {"z":4,"eq":5, "k":5, "f":8}
# def xl(a,b,c,d,e, *args,**kwargs):
#     print(args)
#     print(kwargs)
# xl(5,6,7,8, *[4,], 7,5,6,l=7)

# x = {"z":4,"eq":5, "k":5, "f":8}
# def xl(a,b,c,d,e, **kwargs):
#     # print(args)
#     print(kwargs)
# xl(5,6,7,8, *[4,], k=7,j=5,y=6,l=7)

# x = {"z":4,"eq":5, "k":5, "f":8}
# def xl(a,b,c,d,e,*args, **kwargs):
#     print(args)
#     print(kwargs)
# xl(5,6,7,8, *[4,], x, j=5,y=6,l=7)

# x = {"z":4,"eq":5, "k":5, "f":8}
# def xl(a,b,c,d,e,*args, **kwargs):
#     print(args)
#     print(kwargs)
# xl(5,6,7,8,'t','y', j=5,y=6,l=7)


#21/09/2022
# a = 10 
# b = 20
# def xl(a,b):
#     return a+b
# print(xl(a,b))


# Default args
# if no value is passed for the arg. it will take the default value
# defined in the function definition
# def xl(a,b=7):
#     return a+b
# print(xl(*range(10,12)))







# str
# def xl(a,b, *args):
#     # print(args)
#     print(args[2].dkjgfg())
# xl(1,2,3,4,  'AB')

# kl = {"a":1, "b":2, "ser":2}
def xl(a,b,c, **kwargs):
    print(a)
    print(c)
    print(b)

tr = {"a":4, "b":6, "name":89}
xl(c=5, **tr)
# xl(a=4, b=6, c=89)