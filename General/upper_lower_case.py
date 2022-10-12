char = input("enter character:-")

if ((char >= "A") and (char <= "Z" )):
    print(char, "= is uppercase")
elif((char >= "a") and (char <= "z" )):
    print(char, "= is lowercase")
else:
    print("please inter alphabet number:-")
    char = int(input("enter character:-"))
   
