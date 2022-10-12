#Q1. 1000- amount per 10% discount 
#mximum discount amout only 250 isse jada ka discount nhi de skte

from typing import final


user_amount = int(input("enter user_amount:-"))

if user_amount >= 1000:
    discount = user_amount*10/100
    if discount > 250 :
        discount = 250
    final_discount = (user_amount - discount)
    print(final_discount)    
elif user_amount <= 1000:
    discount = user_amount*5/100
    final_discount = user_amount - discount
    print (final_discount)
else:
    print("wrong")            