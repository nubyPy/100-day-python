# TODO if, else, logical operators
height = int(input("How tall are you? "))


if height >= 120:
    print("Your can ride the rollercoaster")
    age = int(input("How old are you? "))
    price = 0
    if age <= 12:
        print("The price will be $5.")
        price += 5
    elif age <= 18:
        print("The price will be $7")
        price += 7
    elif 45 <= age <= 55:
        print("Free ride.")
    else:
        print("The price will be $12.")
        price += 12
    photos = input("Do you want photos? ").lower()
    if photos == "yes":
        print("You'll have to pay an extra $3.")
        price += 3
    print(f"The total bill is: ${price}")
else:
    print("Sorry, you have to grow taller.")
