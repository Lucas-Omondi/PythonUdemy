print("Welcome to Python Pizza Delliveries!")
size = input("What size pizza do you want? Small, Medium or Large: ")
add_pepperoni = input("Do you want pepperoni? Yes or No: ")
extra_cheese = input("DO you want extra cheese? Yes or No: ")

size = size.upper()
add_pepperoni = add_pepperoni.upper()
extra_cheese = extra_cheese.upper()
if size == "SMALL":
    cost = 15
    if add_pepperoni == "YES":
        cost += 2
elif size == "MEDIUM":
    cost = 20
    if add_pepperoni == "YES":
        cost += 3
elif size == "LARGE":
    cost = 25
    if add_pepperoni == "YES":
        cost += 3
else:
    print("Please input the correct size.")
if extra_cheese == "YES":
    cost +=1

print(f"Your final bill is ${cost}.")
