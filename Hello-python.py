#Define variables
name = []
time = 0
name = input("Who are you? >>>")
if name == "Ethan" or name == "OBrien":
    print("How do you know my name???")
elif name == "Bobert":
    print ("I like pie")
else:
    while time < 10:
        print ("Hello",name)
        time = time + 1
    if input ("Print for infinity? >>>") == "Yes":
        while 1==1:
            print ("Hello", name)
    elif input ("Print different names? >>>") == "Yes":
        while 1==1:
            name = input("What is your name? >>>")
            if name == "stop":
                exit()
            print ("Hello", name)
