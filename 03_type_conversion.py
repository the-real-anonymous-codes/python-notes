# ===================================================
# TYPE CONVERSION
# ===================================================

print("Type Conversion")
print("int() converts into an integer")
print("str() converts into a string")
print("float() converts into a float")
print("bool() converts into a boolean")

print("Any variable can be converted to a STRING using str()")
print("But not every variable can be converted using int() or float()")
print("Every variable can be converted to a boolean using bool()")

num = 23432.9378  # this is a float
print(int(num))    # converts num to int, i.e. 23432
print(str(num))    # converts num to a str, i.e. "23432.9378"
print(bool(num))   # converts num to a bool, i.e. True

print("How does Python decide whether bool() prints True or False?")
print("'Empty' or zero-like values become False, everything else becomes True")
print("For example:")

a = ""
b = 0
c = "d"
d = 0.00
e = "0"
print(bool(a))  # False - empty string
print(bool(b))  # False - zero
print(bool(c))  # True  - non-empty string
print(bool(d))  # False - zero (as a float)
print(bool(e))  # True  - non-empty string (even though it looks like zero!)

print("COMMON MISTAKE: bool('0') is True, not False!")
print("Any non-empty string is truthy in Python, even the string '0'")
print("Only an EMPTY string '' is falsy - the character inside doesn't matter")

print("NOTE: 2.0 == 2 is True in Python, since Python compares the value, not the type")
