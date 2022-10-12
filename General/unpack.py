xlr = [1,2,(1,2,[1,3]), 's', ['a',['b', ('c','d')]], {"my":"name"}]
def checker(el): #el =(1,2,[1,3])  # el =[1,3]
    if type(el) in [list, tuple, set, dict]: # true   # false
        unpacker(el)
    else:
        if type(el) == dict:
            # import pdb;pdb.set_trace()
            for k,v in el.items():
                print(k)
                print(v)
        else:
            print(el)
def unpacker(el):
    for x in el:
        if type(el) == dict:
            for k,v in el.items():
                checker(k)
                checker(v)
        checker(x)
unpacker(xlr)