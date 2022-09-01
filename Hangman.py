import random
from hangman_words import word_list
from hangman_art import logo, stages
print(logo)

chosen_word = random.choice(word_list)
lives = 6

display = []
for _ in range(len(chosen_word)):
    display.append("_")

while not display.count("_") == 0:
    guess = input("Guess a letter: ").lower()
    clear()
    i = 0
    for x in chosen_word:
        if x == guess:
            display[i] = x
        i += 1

    if not guess in chosen_word:
        lives -= 1
        print(stages[lives])

    if lives == 0:
        print("YOU LOST!")
        break

    if "_" not in display: # it is equal to if display.count("_") == 0
        print(f"YOU WON and you have {lives} lives left!")
    str_display = "".join(display)
    print(str_display)

