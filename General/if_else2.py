""" # Indore

Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
Unit                                                     Price  
First 100 units                                               no charge
Next 100 units                                              Rs 5 per unit
After 200 units                                             Rs 10 per unit
(For example if input unit is 350 than total bill amount is Rs2000)"""

"""
# Jabalpur
Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
Unit                                                     Price  
First 100 units                                             0
Next 100 units                                              Rs 10 per unit
After 200 units                                             Rs 15 per unit
(For example if input unit is 350 than total bill amount is Rs2000)
"""
unit = int(input("enter unit:-"))
city = input("enter city name:-")
rates = {
    "indore": {
        "limit_1": 100,
        "limit_2": 200,
        "rate_1": 5,
        "rate_2": 10,
    },
    "bhopal": {
        "limit_1": 100,
        "limit_2": 200,
        "rate_1": 10,
        "rate_2": 15,
    },
}


def bill(unit, city):
    name = rates.get(city)
    if not name:
        return "wrong City"
    limit_1 = name["limit_1"]
    limit_2 = name["limit_2"]
    rate_1 = name["rate_1"]
    rate_2 = name["rate_2"]
    xl = 0
    if unit <= limit_1:
        xl = "no charge"
    elif limit_1 < unit and unit <= limit_2:
        count = (unit - limit_1) * rate_1
        xl = count
    elif unit >= limit_2:
        count = (unit - limit_2) * rate_2
        xl = count + (limit_1 * rate_1)

    return xl


print(bill(unit, city))


"""unit = int(input("enter unit:-"))

def bill(unit, city, f1= 5, f2 = 10):

    if unit == 100:
        print("no charge")
    elif 100< unit <=200:
        count = (unit - 100)*f1
        print(count )
    elif unit >=200:
        count1 = (unit -100)*f2
        print(count1-500)
    else:
        print("wrong")
cit ="indore"
x = 10
y = 15
bill(unit, cit, x , y )  """
