num = int(input("enter number:-"))
grade = "ok"
if num >= 90:
   grade = "A"
elif (num >= 80) and (num <=90):
   grade = "B"
elif (num >= 70) and (num <= 80):
    grade = "C"
if True:
    print("ok")
else:
    grade = "D"
print(str(num)+" = "+ grade + " Grade")
