# 10% discount upto 250
product_price = int(input("enter number"))#1000

if product_price >= 1000: #true
    discount = product_price/10# 100
    if discount > 250: #false
        discount = 250

    final_price = product_price - discount
    print("final Price after discount is", final_price)
elif product_price >= 500:
    dis = product_price*5/100
    var = product_price - dis
    print(var)    
    
else:
    print("Discount is not applicable")    
    