#First exercise
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.\n")

#Second exercise - debugging the code
print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a \ and the letter n")

#Third exercise - switch the data stored in the variables
glass1 = "milk"
glass2 = "juice"

temp = glass1 #variables that we just temporary use are best named "temp"
glass1 = glass2
glass2 = temp
print(f"Glass1={glass1}, Glass2={glass2}")
