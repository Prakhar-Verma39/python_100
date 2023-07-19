print("Weclome to Tresure Island. Your mission is to find the tresure.")
choice = input("left or right?")
if choice.lower() == "right":
    print("Game Over")
elif choice.lower() == "left":
    choice = input("swim or wait")
    if choice.lower() == "swim":
        print("Game Over")
    elif choice.lower() == "wait":
        choice = input("red, yellow or blue?")
        if choice.lower() == "blue":
            print("Game over")
        elif choice.lower() == "yellow":
            print("You Win!")
        elif choice.lower() == "red":
            print("Game Over.")
        else:
            print("Wrong Choice.")
    else:
        print("Wrong Choice.")
else:
    print("Wrong Choice.")