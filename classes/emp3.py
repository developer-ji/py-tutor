class Bus:

    def __init__(self, name=None):
        self.name = name


    __repr__ = 45
    def __repr__(self): 
        if self.name  is not None: 
            return self.name 
        else:
            return 'Name not set'


bus = Bus("i-bus")
empty_bus = Bus()

import pdb; pdb.set_trace()


# print(empty_bus)
# bus # bus.__repr__()
# print(bus) # bus.__repr__()
