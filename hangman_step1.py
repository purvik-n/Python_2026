word_list = ["aardvark", "baboon", "camel"]

import random
chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter: ").lower()
print(guess)

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")


