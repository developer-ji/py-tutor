# Write a program to remove a single  or pair of mid character from string.
import unittest
#Q1
# word = input("Enter word:-") 
# def mid_remover(word):
#     xl = len(word) 
#     mid = xl//2
#     if xl%2 == 0:
#         a = word[:mid-1] + word[mid+1:]
#     else:
#         a = word[:mid] + word[mid+1:]
#     return a

# print(mid_remover(word))

# Q2

word = "my_name_is_manish_and_its_great"

def strip_side(word): #my_name_is_manish_and_its_great
    val  = len(word)
    val_1 = val//2
    result = word[val_1-5:val_1+5]
    return result, 10 # s_manish

def mid_remover(word):
    xl = len(word) #my_name_is_manish_and_its_great
    if xl > 10:
        word, xl = strip_side(word)  # s_manish
    mid = xl//2
    if xl%2 == 0:
        a = word[:mid-1] + word[mid+1:]
    else:
        a = word[:mid] + word[mid+1:]
    return a

print(mid_remover(word))

class MidRemoveTestCase(unittest.TestCase):

    def test_mid_remover(self):
        word = "Prayagraj"
        output = "Praygraj" # 'a' has been removed
        self.assertEqual(mid_remover(word), output)
    def test_mid_remover2(self):
        word = "Prayagra"
        output = "Pragra" # 'ya' has been removed
        self.assertEqual(mid_remover(word), output)

if __name__ == "__main__":
    unittest.main()
