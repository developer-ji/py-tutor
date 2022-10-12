x = [[[[([([([((5))])])])]]]]

y = True
while y:
    x = x[0]

    if type(x) in [list, tuple]:
        continue
    else: break

print(x) 




