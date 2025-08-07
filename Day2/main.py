# THE TIP CALCULATOR
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? -> "))
tip = int(input("What percentage would you like to give? (10, 12 or 15?) -> "))
split = int(input("How many people to split the bill? -> "))

money_per_person = ((bill + (bill * (tip / 100))) / split)
print(f"Each person pays {money_per_person:.2f}")