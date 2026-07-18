# ===================================================
# OPERATORS - Arithmetic, Comparison & Logical
# ===================================================

# ---------------- Arithmetic Operators ----------------

# For maths calculations there are various operators in python given below
# + , - , * , / , // , ** , %
# Operators work for float values too

a = 20
b = 10
c = 30
d = 10.5

# + i.e sum i.e addition
print(a + b + c)      # prints 20 + 10 + 30 i.e 60
print(a + b + c + d)  # prints 20 + 10 + 30 + 10.5 i.e 70.5

# - i.e difference i.e subtraction
print(a - b - c)      # prints 20 - 10 - 30 i.e -20
print(a - b - c - d)  # prints 20 - 10 - 30 - 10.5 i.e -30.5

# * i.e multiply
print(a * b * c)      # prints 20 x 10 x 30 i.e 6000
print(a * b * c * d)  # prints 20 x 10 x 30 x 10.5 i.e 63000

# / i.e division i.e divide
print(a / b)  # prints 20/10 i.e 2.0
print(c / d)  # prints 30/10.5 i.e 2.857142857142857

# // i.e floor division
print(a // b)  # prints int(20/10) i.e 2
print(c // d)  # prints int(30/10.5) i.e 2.0

# ** i.e exponent i.e power i.e index
print(a ** b)  # prints 20^10 i.e 10240000000000
print(c ** d)  # prints 30^10.5 i.e 3234246929812255.5

# % i.e modulus i.e remainder
print(a % b)  # prints remainder of 20/10 i.e 0
print(c % d)  # prints remainder of 30/10.5 i.e 9.0

# ---------------- Operator Precedence ----------------

'''
Order of operations (highest to lowest priority):
() : brackets
** : exponent
* , / , // , % : multiplication, division, floor division, modulus (all at the same level, left to right)
+ , - : addition, subtraction
'''

# ---------------- Comparison Operators ----------------

print("Comparison operators")
print("(== , > , < , >= , <= , !=)")
# equal to, greater than, less than, greater or equal, less or equal, not equal
# comparison operators always give a bool value as output

print(12 == 13)         # False
print(12 > 14)           # False
print(145 < 23456789)    # True
print(120 <= 120)        # True
print(1234 >= 1)         # True
print(12 != 12)          # False
print(22 != 21)          # True

# ---------------- Logical Operators ----------------

print("Logical operators")
print("and , or , not")

print("If any condition is False, the 'and' operator prints False")

print((2 == 2) and (9 != 9))                        # one condition True, one False, 'and' used -> False
print((3 > 22) and (788 <= 789) and (334 == 344))    # two conditions False, one True, 'and' used -> False
print((2 == 2) or (0 < 343) or (23 >= 22))           # all conditions True, 'or' used -> True

print("If any condition is True, the 'or' operator prints True")

print((2 == 2) or (9 != 9))                          # one condition True, one False, 'or' used -> True
print((3 > 22) or (788 <= 789) or (334 == 344))      # two conditions False, one True, 'or' used -> True
print((2 == 3) or (0 > 343) or (23 <= 22))           # all conditions False, 'or' used -> False

print("'not' flips True into False and False into True")
print(not True)   # False
print(not False)  # True
