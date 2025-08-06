#transfer a line to comment with ctrl + / (left to R shift)
print("Hello World!\nHelloWorld!") #new line = \n
print("Hello" + " " +"Angela") #string concatenation - merging strings into one

print("Hello " + input("What is your name? -> ")+"!") #this line of code will take the users input using the input() function

name = input("What is your name? -> ") #name is a variable that stores the data from the input() function

#Take in the users input and print out the length of it
print(len(input("What is your name? -> ")))

#Store the user input into variables and print out the length of it
username = input("What is your name? -> ")
username_length = len(username)

print(f"The length of your name is: {username_length}")
