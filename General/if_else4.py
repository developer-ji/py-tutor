# Q2. Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
    
#         Cost price (in Rs)                                       Tax
#         > 100000                                                  15 %
#         > 50000 and <= 100000                          10%
#         <= 50000                                                  5%
cost_price = int(input("enter price of bike:-"))

def calculate_road_tax(bike_price):
    road_tax = 0
    if bike_price >= 100000:
        road_tax = bike_price*15/100
    elif (bike_price >= 50000) and (bike_price >= 100000):
        road_tax = bike_price*10/100
    elif bike_price <=50000:
        road_tax = cost_price*5/100
    return road_tax

print("Applicale Road Tax = ", calculate_road_tax(cost_price))
