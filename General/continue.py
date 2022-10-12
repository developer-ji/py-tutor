# x = [1,2]#,3,5]

# for i in x: #i = 1 
#     if i < 2: # 1 <2 true
#         print(i) # 1
#     elif i >= 2: 
#         pass
#     print(i)# i = 1

# for i in x: #i = 2 
#     if i < 2: # 2 < 2 false
#         print(i) # 1
#     elif i >= 2: # 2 >= 2 true
#         continue
#     print(i)# i = 2

# 1 
# 1
# 2
def process_salary(name): # aman
    print("salary credited for ", name)# salary credited for namrta
def give_bonus(name):
    print("Bonus Processed for ", name)# Bonus Processed for rahul

names =['aman', 'pritam', 'naman', 'rahul', 'namrta']
for name in names: # name = namrta
    process_salary(name) # 
    if name == "rahul": # false
        break
    give_bonus(name)
#salary credited for aman
# Bonus Processed for aman
# salary credited for pritam
# Bonus Processed for pritam
# salary credited for naman
# Bonus Processed for naman
# salary credited for rahul
# Bonus Processed for rahul
# salary credited for namrta
# Bonus Processed for namrta

    
