print("Welcome to Treasure Island")
print("Your missin is to find the Treasure.")
while True:
    # crossroad choice
    crossroad = input("You are at a crossroad. Where do you want to go? Left or Right?\n").lower()
    if crossroad == "left":
        while True:
            # lake choice
            lake = input("You have come upon a lake. Type 'wait' to wait for a boat and 'swim' to swim across \n").lower()
            if lake == "wait":
                island = input("You arrive at the island unharmed. There is a house with 3 doors, one red, one yellow and one blue. Which color do you choose?\n")
                island = island.lower()
                if island == "red":
                    print("You were burnt by fire dragon. GAME OVER!!")
                    break
                elif island == "blue":
                    print("You were frozen by ICE BREATH. GAME OVER!!")
                    break
                else:
                    print("HOORAYYYYYY!!!! YOU OBTAINED THE TREASURE!")
                    break
            else:
                print(" Ooops. You were eaten by a crocodile. GAME OVER!!!!")
    
    elif crossroad == "right":
        print("GAME OVER!!")  
        break
    else:
        print("Please choose a correct path.") 
