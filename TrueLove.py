
print("Welcome to the Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.upper()
name2 = name2.upper()
T = name1.count("T") + name2.count("T")
R = name1.count("R") + name2.count("R")
U = name1.count("U") + name2.count("U")
E = name1.count("E") + name2.count("E")
TRUE = str(T+R+U+E)

L = name1.count("L") + name2.count("L")
O = name1.count("O") + name2.count("O")
V = name1.count("V") + name2.count("V")
E = name1.count("E") + name2.count("E")
LOVE = str(L+O+V+E)
SCORE = int(TRUE + LOVE)
if SCORE <10 or SCORE >90 :
    print(f"Your score is {SCORE}, you go together like coke and mentos")
elif SCORE >40 and SCORE<50:
    print(f"Your score is {SCORE}, youre alright")
else:
    print(f"Your score is {SCORE}")