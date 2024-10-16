height = int(input("Enter your height in m: "))
cost = 0

if height >= 120:
    print("You can ride the Rollercoaster!!")
    age = int(input("Enter your age: "))
    if age < 12:
        cost +=5
    elif age < 18:
        cost += 7
    else:
        cost += 12
        if age >= 45 and age <= 55:
            cost = 0
    photos = input("Woud you like photos taken? YES or NO: ") 
    photos = photos.upper()
    if photos == "YES":
        cost += 3
    print(f"Your total bill is ${cost}")
else:
    print("Unfortunately you cannot ride the rollercoaster.")