List = ['x', 'y', 'z', [[1,2],3,],'b', ('a','b'), {1,2,3}, None, '', [],'', False, (), {}]   

for i in List:
    if type(i) == list:
        for x in i:
            if type(x) == list:
                for y in x:
                    print(y)
    elif type(i) == tuple:
        for a in i:
            print(a)
    elif type(i) == set:
        for b in i:
            print(b)
    elif not i:
        pass       
    else:
        print(i)
print("\nAll has been printed")