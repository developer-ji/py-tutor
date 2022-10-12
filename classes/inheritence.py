# class Parent:
#     name = "parent class"


# class Child(Parent):
#     pass

# class SubChild(Child):
#     namert = "Sub Child"

# class MoreSubChild(Child):
#     pass

# child = MoreSubChild()
# print(child.name)

# child = SubChild()
# print(child.namert)

#Q2
# class Chaturbhuj:

#     def __init__(self , left, right, top, bottom):
#         self.left = left
#         self.right = right
#         self.top = top
#         self.botton = bottom

#     def perimeter(self):
#         return self.left+self.right+self.top+self.botton

#     def is_rectangle(self):
#         if self.left == self.right and self.top == self.botton:
#             return "this is rectangle"
#         return "this is not rectangle"



# kl = Chaturbhuj(*[2,1,2,2])
# yl = Chaturbhuj(*[3,2,3,2])

# print(kl.pramee())
# print(yl.pramee())
# print(kl.is_rectangle())


#Q3
# class Triangle:

#     def __init__(self , base, hight, slant):
#         self.base = base
#         self.hight = hight
#         self.slant = slant

# xl = Triangle(5,5,7 )   
# print(xl.base)     
# print(xl.hight)     
# print(xl.slant)     

from tiger.perimeter import perimeter
print(perimeter(*range(4)))