# Iterable
# Collections(list , tuple, set, dictionary), string
# String = 'random_string'  # Int = 12344
# xl = ('a', 'b')
# for x in xl: print(x)
# a
# b
# List = ['x', 'y', 'z', 'b', ('a','b')]
# for i in List:
#     if type(i) == tuple:
#         for x in i: 
#             print(x)
#     else: print(i)

# xl = [1,2,3,4,5, 6]
# for i in xl:
#     if i%2 == 0:
#         print(i, "is even number")
#     else:
#         print(i, "is odd number")    

# List = ['x', 'y', 'z', [1,2,3,],'b', ('a','b')]
# for i in List: # i = x
#     if type(i) == list: # false
#         for x in i:  # x=1
#             print(x)
#     elif type(i) == tuple:
#         for y in i:
#             print(y)
#     else:
#         print(i)
# 

# # List = [[[1,2],3,]]
# for i in List: # i = [[1,2],3,] 
#     if type(i) == list: # true
#         for x in i:  # x = 3  for loop 3 ko lene wapas gaya tha uper
#             if type(x) == list: # false
#                 for y in x: # y = 2
#                     print(y) # 1  #2
#             elif type(i) == tuple:
#                 for y in i:
#                     print(y)
#             elif type(i) == set:
#                 for z in i:
#                     print(z)
#             else:
#                 print(i)
   
# List = ['x', 'y', 'z', [[1,2],3,],'b', ('a', 'b'), {1,2,3}]   
# for i in List: 
#     if type(i) == list: 
#         for x in i:  
#             if type(x) == list: 
#                 for y in x: 
#                     print(y)
#     elif type(i)== tuple:
#         for z in i:
#             print(z)
#     elif type(i) == set:
#         for p in i:
#             print(p)
#     else:
#         print(i)

   


xlr = [1,2,(1,2,[1,3]), 's', ['a',['b', ('c','d')]]]
def checker(el): #el =(1,2,[1,3])  # el =[1,3]
    if type(el) in [list, tuple, set, dict]: # true   # false
        unpacker(el)
    else:
        print(el)
def unpacker(el): #el =[(1,2,[1,3]), 's', ['a',['b', ('c','d')]]]   # el = ([1,3])  # [1,3]
    for x in el:  #x =(1,2,[1,3]) # x = [1,3]
        checker(x)
unpacker(xlr)


                           