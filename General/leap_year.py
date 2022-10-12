x = int(input("enter year:-")) # 2000

if x%4 == 0:
    if x%100 == 0:
        if x%400 == 0:
            print("leap year")
        else: print("Not leap year")
    else:
        print("leap Year")
else: print("Not leap year")
