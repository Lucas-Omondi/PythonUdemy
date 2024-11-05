import random
result = random.randint(1, 100)
print('Welcome to Guessing Game\n')
level = input('Pick a difficulty level: Hard or Easy: ')
level = level.lower()

count = 1
if level == 'hard':
    lifes = 5
    print('You have 5 tries to guess a number between 1 and 100\n')
    while count <= lifes:
        guess = int(input("Guess the number: "))
        if guess == result:
            print('Congratulations! You guessed the correct number!')
            break
        elif guess > result:
            print('Too high!')
            count += 1
            continue
        else:
            print('Too low!')
            count += 1
            continue
else:
    lifes = 10
    print('You have 10 tries to guess a number between 1 and 100\n')
    while count < lifes:
        if count < lifes:
            guess = int(input("Guess the number: "))
            if guess == result:
                print('Congratulations! You guessed the correct number!')
                break
            elif guess > result:
                print('Too high!')
                count += 1
                if count == lifes:
                    print("Oops you are out of lives")
                continue
            else:
                print('Too low!')
                count += 1
                if count == lifes:
                    print("Oops you are out of lives")
                continue
        else:
            print("Oops you are out of lives")