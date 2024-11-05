import random
from hangman_art import *
from hangman_words import *

print(logo)
computer_choice = random.choice(word_list)
print(computer_choice)
display = []
lives = 6

# Making display as long as the chosen word
for letter in computer_choice:
    display.append("_")

#Looping until all blanks are filled
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ")
    if guess in display:
        print("You have already guessed that letter")
    guess = guess.lower()
    position = 0
    if guess in computer_choice:
        for position in range(len(computer_choice)):
            if computer_choice[position] == guess:
                display[position] = guess
        print(display)
        print(stages[lives])
        if "_" not in display:
            end_of_game = True
            print("You WIN!!")
    else:
        lives -= 1
        print(f"Sorry {guess} is not in the word.")
        print(f"You have {lives} guesses left.")
        print(display)
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("Game over, You LOSE!!")


