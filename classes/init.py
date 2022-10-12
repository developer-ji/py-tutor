from datetime import datetime
class Name:
    def __init__(self,  *arg, **kwargs):
        self.created_at = datetime.now()
        print("Initialization done") 

    # def __str__(self):
    #     return "name of class is Name"

x = Name() # initialize

import pdb; pdb.set_trace()