# Iterable
# Containers (list , tuple, set, dictionary), string 
## List comprehension

# kl = [x if x> 5 else 0 for x in range(20)]

# kl = []
# for x in range(20):
#     if x> 5:
#         kl.append(x)
#     else:
#         kl.append(0) 

list1 = [1,2,34,5,6]
tuple1 = (1,2,345654,5,6)
set1 = {1,2,34,5,6}

dict1 = {"a":1,"b":2,"c":34,"d":5,"e":6}

# for x in list1:
#     print(x)
# print("\n")
# for x in tuple1:
#     print(x)
# print("\n")

# for x in set1: # x = 1
#     print(x)
# for x in dict1.keys():
#     print(x)

# list2 = [ (1,2), (3,4), (5,6), (7,[8,9])]

# for x,y in list2: # x,y = (1,2)
#     print(x)

# # Enumerate gives indexing
# for i,x in enumerate(list1): 
#     print(i,x)


# list1 = [1,2,34,5,6]
# set1 = {"ams", "bhopla", "name", "sdfsd", "sdfsd"}
# ## zip we can iterate through multiple iterable(Jisme hum for loop laga skte hain) at once
# for x,y,z in zip(list1, set1, tuple1):
#     print(x,y,z)

# word = input("Enter name:-")
#"amkank"
# a = 2
# m = 1
# n = 1
# k = 2
# word_of_counts = {item:word.count(item) for item in word }
# print(word_of_counts)


# word = input("Enter name:-")
# c = 0
# for x in word:
#     if x == :
#         c = c+1
#     elif x == "a":
        
# print(c)

# word = "amarkantak"
# chars_list =['a', 'm']
# count = [1,1]


# for x in word:
#     if x  not in chars_list:
#         chars_list.append(x)
#         count.append(1)
#         xl = count[1]+1
#         count[0] = xl

word = "amarkantak"
kl = []
xl = []

for x in word:
    if x not in kl:
        kl.append(x)
    elif x in kl and x not in xl:
        xl.append(x)

print(kl)  
print(xl)  


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
# xlr = input("Enter word:- ")  # amarkantak
# usr = input("Enter character:- ") # 'k'
# count = 0
# for i in xlr:
#     if i == usr:
#         count = count+1
# print(count)


# def xl(ch):
#     x = 0
#     for i in xlr:
#         if i ==  ch:
#             x = x + 1
#     return x
# xl(usr)


    



    