num1 = input("enter first number:-")
num2 = input("enter second number:-")
num3 = input("enter three number:-")

if (num1>num2) or (num1>num3):
    print("maximum = ",num1)
elif (num2>num3):
    print("maximum =", num2)
else:
    print("maximum = ", num3)