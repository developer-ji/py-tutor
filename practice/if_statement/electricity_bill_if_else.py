'''Q1  Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
             Unit                                                     Price  
First 100 units                                               no charge
Next 100 units                                              Rs 5 per unit
After 200 units                                             Rs 10 per unit
(For example if input unit is 350 than total bill amount is Rs2000)'''

unit = int(input("enter unit:-"))

if unit == 100:
    print("no charge")
elif 100< unit <=200:
    count = (unit - 100)*5
    print(count)
elif unit >=200:
    count1 = (unit -100)*10
    print(count1-500)    

else:
    print("wrong") 