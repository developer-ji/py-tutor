

class Run
|---------------------------------|                          
|                                 |
|      A  = 30                    |
|      B   = 30                   |
|                                 |
|                                 |
|---------------------------------|

run = Run()
run.A =  50 # set krna
run.A
run.name
run.name = "first"
run.name # "first" 
run.xtr =  kum 
print(run.xtr())
|---------------------------------|
|                                 |
|      A  = 50                    |
|      B   = 30                   |
|      name = "first"             |
|       def xtr():    a+b         |
|                                 |
|---------------------------------|


quit = Run()
quit.A # print30
quit.name 
|---------------------------------|
|                                 |
|      A  = 30                    |
|      B  = 30                    |
|      x  = 45                    |
|                                 |
|---------------------------------|


class str
|---------------------------------|
|      def title(self, *args):    |
|            pass                 |
|      A  = 30                    |
|      B   = 30                   |
|                                 |
|                                 |
|---------------------------------|

x = str('df')
x.title  # Get krna
x.title = ty # set krna
|---------------------------------|
|      def title(self, *args):    |
|            pass                 |
|      A  = 30                    |
|      B   = 30                   |
|                                 |
|                                 |
|---------------------------------|


def __init__(self): pass
def __name__(self): pass
def __new__(self): pass


from datetime import datetime

class Name:
    def __init__(self,  *arg, **kwargs):
        self.created_at = datetime.now()
        print("Initialization done") 

    def __str__(self):
        return "name of class is Name"

a = Name() # initialize
