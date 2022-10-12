# generatoer me 2 for loop lagne se pahli for loop ko jaha tak range dege vah tak chale gi but dusri for loop me jis range tak pahli for loop chali thi uske bad se loop chale gi generator stating ke loop ko skip kar dega


li = [
    "apple",
    "orange",
    "banana",
    "elephant",
    "shark",
    "whale",
    "dog",
    "cat",
    "mice",
    "uncle",
    "cute",
    "nice",
    "correct",
]
generated_list = (x for x in li)  #generator ko tuple me  hi likhte hai
print("type of generated_list is ", type(generated_list)) #type iska generator hai
# import sys   
# sys.exit()
count = 0
for i in generated_list:
    if count > 2:
        break
    print(i)
    count += 1
count = 0
for i in generated_list:
    if count > 2:
        break
    print(i)
    count += 1

# apple
# orange
# apple
# orange