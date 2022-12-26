# a = [7,10,9,6,3]
# b = [4,3,1,8,5]
# c = []
# d = []
# for i in a:
#     if i in b:
#         c.append(i)
#     else:
#         d.append(i)
# print(c)
# print(d)

word_1 = "amarkantak"
word_2 = "allahabadk"
common = [] 
count = 0
for i in word_2:
    if i in word_1 and i not in common:
        common.append(i)
        count+1
        
        
    
print(common)
# print(one_time)
# user = int(input("enter number:-"))



# see = user//24
# rem = user % 24
# for _ in range(see):
#     for i in range(24):
#         if i <10:
#             print("0"+str(i)+":00")
#         else:
#             print(str(i)+":00")
# if rem:
#     for i in range(rem):
#         if i <10:
#             print("0"+str(i)+":00")
#         else:
#             print(str(i)+":00")

user = int(input("enter number:-"))
def hours(rem):
    for i in range(rem): print("0"+str(i)+":00") if i <10 else print(str(i)+":00") 

see = user//24
rem = user % 24
for _ in range(see): hours(24)
if rem: hours(rem)