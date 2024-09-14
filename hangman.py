import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

#Todo 1: Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += " _ "
print(placeholder)

guess = input("guess a letter: ").lower()
print(guess)

for letter in chosen_word:
    if letter == guess:
        print("right")
    else: 
        print("Wrong")

display = "_"
    