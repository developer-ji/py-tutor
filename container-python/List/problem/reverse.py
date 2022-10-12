# list1 = "Nisha Shukla"
# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print(list1)
# for i in list1[::-1]:
#     print(i)

# print([*list1])  # Unpacking
# print([*reversed(list1)])
# print(''.join(reversed(list1)))

#Q2
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# list3 = []

# for i, y in zip(list1,list2):
#     list3.append(i+y)
# print(list3)

#Q3
# numbers = [1, 2, 3, 4, 5, 6, 7]

# for i,x in enumerate(numbers):
#     numbers[i] = x*x
# print(numbers)

# Q4
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

for x in list1:
    for y in list2:
        print(x+y)
