# Treasure island minigame
print("Welcome to Treasure Island!\nYour mission is to find the treasure.")

decision1 = input(f"You're at a cross road. Where do you want to go?\n    Type 'left' or 'right'\n").lower()
if decision1 == "right":
    print("You fell into a hole.\nGame over!")
else:
    decision2 = input("You arrived to a lake. There is an island in teh middle of the lake.\n    Type 'wait' to wait for a boat or 'swim' to swim across.\n").lower()
    if decision2 == "swim":
        print("Attacked by trout.\nGame over!")
    else:
        decision3 = input("You arrived at the island unharmed. There is a house with 3 doors.\n    One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if decision3 == "red":
            print("Burned by fired.\nGame over!")
        elif decision3 == "blue":
            print("Eaten by beasts.\nGame over!")
        else:
            print("You won!")