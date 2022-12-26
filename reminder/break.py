def process_salary(name):
    print("process salary",name)
def give_bonus(name):
    print("give_bonus",name)

names = ["nisha","akshy","ajay","neeraj"]

for name in names:
    process_salary(name)
    if name == "ajay":
        continue          #continue ajay ko bonus nhi dga or sabhi ko dega
        # break           #breake ajay ke bad se code ruk jaye ga
        #pass             #pura code run hoga or sabhi ko salary or bonus milega
    give_bonus(name)
