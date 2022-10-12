# class A:
#     y = 6
#     def xl(self,  *args, **kwargs):
#         y = 20
#         self.yl(5)

#     def yl(self,x):
#         print(x)
#         print("yl")
#         print(self.re)
#     re = 50

# # list
# a = A() # instance of class A
# a.xl(6, *range(4))
# # a.yl(8)



# class Name:
#     y = 20
#     def xl(self,  *args, **kwargs):
#         self.yl(5)
#         print(self.trs)
#     def yl(self,x):
#         print(x)
#         print("yl")
#         print(self.re)
#     re = 50

# a = Name() 
# a.trs = "Nisha"
# a.xl()

# b = Name() 
# b.xl()

class Name:
    y = 20
    def xl(self,  *args, **kwargs):
        print(args) #(a,)
        print(args[0]) # a.__main__A
        print(args[0].trs)

a = Name() 
a.trs = "Nisha"
# a = 45
print("\n---------------------||--------------------------\n")
b = Name() 
b.trs = "Rinku"
b.xl(a)




