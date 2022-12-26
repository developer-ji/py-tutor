Bus = {

    __str__ = "my name"

    def __init__(self, name=None):
        self.name = name

    def __repr__(self): 
        if self.name  is not None: 
            return self.name 
        else:
            return 'Name not set'
}

bus = Bus("sdsd")

bus = {
    __str__ = "my name"

    def __init__(self, name=None):
        self.name = name #set 
        self.kl = name #set 

    def __repr__(self): 
        if self.name  is not None: 
            return self.name 
        else:
            return 'Name not set'
    name = name
    kl = name
}

bus.info

