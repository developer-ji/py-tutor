#Q1
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# list2.reverse()
# for k,y in zip(list1,list2):
#     print(k,y)

# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# list1.remove("")
# list1.remove("")
# print(list1)

#Q2
from dataclasses import replace
from os import remove


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# print(len(list1))
# list2 = list1[2]
# list3 = list2[2]
# list3.append(7000)
# print(list1)

#one line code
# list1[2][2].append(7000)
# print(list1)


#Q3
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
# list2 = list1[2]
# list3 = list2[1]
# list4 = list3[2]
# list4.extend(sub_list)
# print(list1)

# one line code
# list1[2][1][2].extend(sub_list)
# print(list1)

#Q4
# list1 = [5, 10, 15, 20, 25, 50, 20]
# list2 = list1.index(20)
# list1[list2]= 200
# # print(list2)
# print(list1)

#Q5
list1 = [5, 20, 15, 20, 25, 50, 20]
list2 = []
for i in list1:
    if i != 20:
        list2.append(i)
print(list2)
