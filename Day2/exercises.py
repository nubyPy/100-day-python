# First exercise - fixing code: print("Number of letters in your name: " + len(input("Enter your name")))
print("Number of letters in your name: " + str(len(input("Enter your name"))))

# Second exercise - change the code so the output is 3: print(3 * 3 + 3 / 3 - 3)
print(3 * ((3 + 3) / 3) - 3)

# Third exercise - BMI calculator (weight divided by height squared)
height = int(input("How tall are you in cm? -> "))
weight = int(input("How much do you weight in kg? -> "))
bmi = weight / ((height / 100) ** 2)

print(f"BMI value is: {round(bmi, 2)}")
