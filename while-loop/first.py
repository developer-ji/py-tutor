names = ["a", "b", "c", "d", "e", "f"]

x = 'o'
c = 0

while x:
    if c < len(names):
        x = names[c]    
    else:
        x = None
    c += 1
    print("I am printing", x)
   