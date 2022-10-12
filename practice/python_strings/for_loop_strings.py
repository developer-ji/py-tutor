#Q1
# a = "heello"
# count = 0
# for i in a:
#     if i == "h":
#         count = count+1
# print("count= ",count)  

# #Q2
# Name = input("Enter name:-")
# user = input("Enter char:-")
# count = 0
# for i in Name:
#     if i == user:
#         count = count+1
# print("count= ", count)

#Q3
# xlr = input("enter name :-")
# user1 = input("enter char:-")
# def name(ch):
#     x = 0
#     for i in xlr:
#         if i == ch:
#             x = x+1
#     return x
# print("count= ", name(user1))


#Q4
word_1 = "amarkantak"
word_2 = "allahabadk"
common = []
remove_duplicate = []

for i in word_2:
    if i in word_1 and i not in common:
        common.append(i)
    else:
        remove_duplicate.append(i)

print("common= ",common)
print("remove_duplicate= ",remove_duplicate)


one_time = []
for i in remove_duplicate:
    if i not in one_time:
        one_time.append(i)
print("one_time= ", one_time)
