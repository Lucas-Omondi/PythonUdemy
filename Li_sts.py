rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

options = [rock, paper, scissors]
my_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n")
player_choice = options[int(my_choice)]
computer_choice = random.choice(options)
if player_choice == computer_choice:
    print(f"You chose {player_choice}\n")
    print(f" Computer chose {computer_choice}")
    print("It's a tie!")
elif player_choice == rock:
    print(f"You chose {player_choice}\n")
    if computer_choice == paper:
        print(f"Computer chose {computer_choice}\n")
        print("You lose!")
    else:
        print(f"Computer chose {computer_choice}\n")
        print("You win!")
elif player_choice == paper:
    print(f"You chose {player_choice}\n")
    if computer_choice == scissors:
        print(f"Computer chose {computer_choice}\n")
        print("You Lose!")
    else:
        print(f"Computer chose {computer_choice}\n")
        print("You Win!")
elif player_choice == scissors:
    print(f"You chose {player_choice}\n")
    if computer_choice == paper:
        print(f"Computer chose {computer_choice}\n")
        print("You Win!!")
    else:
        print(f"Computer chose {computer_choice}\n")
        print("You Lose!")
