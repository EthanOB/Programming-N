i = 0
MainIdeas = ["state", "conditionals", "loops", "functions"]

if input("Is complexity one of the main ideas?").lower() == "no":
    print("Good Job. You got it right.")
    i = i + 1
else:
    print("Sad day. You choose wrong")
if input("Is sequence one of the main ideas?").lower() == "yes":
    if i == 1:
        print("Wow, epic. You got it two right in a row.")
    else:
        print("Nice. You got it right.")
    i = i + 1
else:
    print("You got it wrong.")
if input("What is one of the other ideas?").lower() in MainIdeas:
    i = i + 1
    print("nice")
else:
    print("You got it wrong.")
if i == 3:
    print("Wow, You got them all right.")
if i == 2:
    print("You only got one wrong.")
if i == 1:
    print("You only got one right.")
if i == 0:
    print("Wow, you got all of them wrong. Mr. Lowe is disappointed.")
print(f"you got {round(i* 100/3)}% right")
