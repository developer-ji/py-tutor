'''break statement me jaha pe break lagaye ge vahi se stop ho jaye ga'''
#Q1
# print("break_statements:-")
# for i in range(11):
#     if i == 5:
#         break
#     print(i)

# #Q2
# lis = ["banana", "apple","orange"]
# for i in lis:
#     if i == "apple":
#         break
#     print(i)
# #Q3
def processes_salary(name):
    print("processes salary")
def give_bonus(name):
    print("give bonus")
names = ["nisha","rahul", "riya","deep"]
for i in names:
    processes_salary(i)
    if (i == "rahul"):
        continue
    
    give_bonus(i)

