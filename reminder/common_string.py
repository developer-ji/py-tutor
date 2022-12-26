word_1 = "amarkantak"
word_2 = "allahabadk"
common = [] 
one_time = []
count = 0
for i in word_1:
    if i in word_2 :
        common.append(i)
    else:
        one_time.append(i)
print("common",common)
print("one_time",one_time)





#Q2
# word_1 = "amarkantak"
# word_2 = "allahabadk"
# common = [] 
# count = 0
# for i in word_1:
#     if i in word_2 and i not in common :
#         common.append(i)
#         count = count+1

# print(common)