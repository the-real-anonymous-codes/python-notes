# ===================================================
# INPUT & OUTPUT
# ===================================================

print("To take input from the user we use the input() function")

name = input("Enter your name: ")
print("A value entered by the user is always saved as a str")
print("To convert it into int, float, or boolean we use the int(), float(), and bool() functions respectively")

age = int(input("Enter your age: "))

print("There are two ways to give output")

# 1st way: use one or more strings separated by commas
print("Hi", name, "you are", age, "years old")

# 2nd way: use an f-string
print(f"Hi {name} you are {age} years old")
