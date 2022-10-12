import datetime 
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

#Creating Date Objects
y  = datetime.datetime(2021, 3, 3)
print(y)



date_object = datetime.date.today()
print(date_object)