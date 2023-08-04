import random
import time
print(" Hello, Welcome to the Anagram_Maker App ")
string = input(" Type a word you want to jumble up: ")
word_list = []
word_string = ""
for letter in string:
    word_list.append(letter)
time.sleep(2)
print(word_list)
for i in range(len(word_list)):
    c = random.choice(word_list)
    word_list.remove(c)
    word_string += c
time.sleep(2)
print(f"The anagram for '{string}' is '{word_string}'!")