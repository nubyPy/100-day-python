# TODO Learning data types
# Subscripting - printing out a specific character from a string
print("Hello!"[5])
print("Hello!"[-1]) # can start from negative

# Large integers
print(123_456_789) # You can only see the _ in the code, in the output it will be: 123456789

# Float
print(3.14159)

# Boolean
print(True)
print(False)

# Type checking - returns the type of data
print(type("Hello"))
print(type(12345))
print(type(True))
print(type(3.14159))

# Type conversion - changing data types
print(int("123") + int("456"))

# Division
print(6 / 3)
print(6 // 3) # cuts the float part
print(2 ** 4) # 2 to the power of 4

# Number rounding
bmi = 65 / 1.65 ** 2
print(f"BMI is {round(bmi, 2)}")
