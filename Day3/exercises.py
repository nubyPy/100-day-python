# First exercise - even or odd number
number = int(input("Odd or even number? -> "))

if number % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")

# Second exercise - BMI calc with interpretations

weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("overweight")

# Third exercise - pizza delivery

size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? yes or no: ").lower()
cheese = input("Do you want extra cheese? yes or no: ").lower()
price = 0

if size == "s":
    price += 15
    if pepperoni == "yes":
        price += 2
if size == "m":
    price += 20
if size == "l":
    price += 25
if size == "m" or "l" and pepperoni == "yes":
    price += 3
if cheese == "yes":
    price += 1
print(f"Your pizza will be: ${price}")
