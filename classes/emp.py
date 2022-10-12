
class Employee:
    # name = "user name"
    # address = "Empty address"
    # emp_type = "Part Time / Full Time"
    
    def __init__(self, *args, **kwargs):
        self.name  =kwargs["name"]
        self.address = kwargs.get("address", "default address")
        self.emp_type = kwargs["emp_type"]


    def info(self):
        print("name = ", self.name)
        print("address = ", self.address)
        print("emp_type = ", self.emp_type)
    

emp1_name ="Ajay"
emp1_address ="Vijay Nagar"
emp1_type ="full time"

emp2_name ="Shruti"
emp2_address ="Navlakaha"
emp2_type ="part time"

emp1 = Employee(name = emp1_name, address = emp1_address, emp_type = emp1_type ) #initialization
emp1.info()
emp2 = Employee(name = emp2_name, address = emp2_address, emp_type = emp2_type)
emp2.info()

emp3_name = "Neeraj"
emp3 = Employee(name = emp3_name, emp_type = "Srf")
emp3.info()
