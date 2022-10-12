import datetime

c = 0

while True:
    x = datetime.datetime.now()
    y = str(x)
    print(y[20:])
    c += 1
    xlr = [ int(i) for i in y[20:] ]
    if sum( xlr ) > 45:
        break

if c > 100000:
    print("You have won")
    print("\n\n______",c,"________\n\n")
else:
    print("You have Lost")
    print("\n\n______",c,"________\n\n")
