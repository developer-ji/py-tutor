word = input("Enter word:-")

def side_remover(word):
    xl = len(word) #my_name_is_manish_and_its_great
    side = xl//2
    if xl%2 == 0:
        a = word[side-1] + word[side]
    else:
        a = word[side]
    return a
print("Remove_side_word:- ", side_remover(word))


# word = input("Enter word:-")

# def side_remover(word):
#     xl = len(word) #manish yuneesh
#     side = xl//2
#     side1 = side//2
#     if xl%2 == 0:
#         a = word[side1] + word[side1+1:5]
#     else:
#         a = word[side1+1] + word[side1+2]
#     return a
# print("Remove_side_word:- ", side_remover(word))


# word = input("Enter word:-")

