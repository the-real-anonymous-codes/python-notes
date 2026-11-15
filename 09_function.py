# ===================================================
# FUNCTIONS
# ===================================================

# To avoid writing the same code again and again, we use functions.
# Python has many built-in functions, and we can also create our own.
# A function is defined using the keyword def.

# Example 1: simple function

def add(a, b):
    print(a + b)


add(10, 20)      # 10 and 20 are arguments
add(3, 5)        # here a = 3 and b = 5

# In the function above, a and b are parameters.
# Parameters are variables defined inside the function.
# Arguments are the actual values passed when calling the function.

# Example 2: function with return value

def multiply(a, b):
    return a * b


result = multiply(4, 6)
print(result)

# A function can return a value using the return keyword.
# Without return, the function prints or does something but returns None.

# Example 3: palindrome check

def is_palindrome(number):
    original = number
    reverse = 0

    while number > 0:
        reverse = reverse * 10 + number % 10
        number = number // 10

    if reverse == original:
        print(f"{original} is a palindrome number")
    else:
        print(f"{original} is not a palindrome number")


is_palindrome(121)
is_palindrome(456)
is_palindrome(12321)

# Types of arguments

# 1) Positional arguments
# Order matters

def product(a, b, c, d):
    print(a * b * c * d)


product(3, 2, 1, 3)
# Here a = 3, b = 2, c = 1, d = 3

# If we call:
# product(2, 4, 4)
# It will raise an error because d is missing.

# 2) Default arguments
# If no value is passed for an argument, Python uses the default value.

def add_with_default(a, b, c=445):
    print(a + b + c)


add_with_default(23, 23)      # c will use the default value 445
add_with_default(10, 20, 30)  # c is passed explicitly

# Note: once you assign a default value to a parameter,
# you should not place non-default parameters after it.

# 3) Keyword arguments
# We can pass values by parameter name in any order.

def subtraction(a, b):
    print(a - b)


subtraction(a=36, b=34)
# Positional arguments cannot come after keyword arguments.

# Example of function with two parameters and default value

def greet(name="friend"):
    print(f"Hello, {name}!")


greet()
greet("Alice")

# Functions make code reusable, easier to read, and easier to maintain.
