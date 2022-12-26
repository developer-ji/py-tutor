li = [7,10,9,6,3]
l = [4,3,1,8,5]
duplicate = []
one_time = []
for i in li:
    if i in l:
        duplicate.append(i)
    else:
        one_time.append(i)
print(duplicate)
print(one_time)