# from operator import index
# import random
# def gener_list():
#     return list(range(1,11))
# x = gener_list()
# # import pdb; pdb.set_trace()
# print(random.choice(x))
# print(random.choices(x,k=3))
# print(random.choices(range(100),k=10))
# random.shuffle(x)
# print(x)
# val = x.index(10)
# print(val)
# num = range(100)
# random.choices(num,k=10)
# print(random.choices(num,k=10))

# Q2
num = [2, 29, 70, 11, 43, 39, 71, 18, 58, 23]
def sort_num(x_num):
    x = 0
    for i in x_num:#2 ,29
        if i >= x:#2 ,29
            # print(i)
            x = i
    return x
print(sort_num(num))

