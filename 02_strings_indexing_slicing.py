# ===================================================
# STRINGS - UNICODE, INDEXING & SLICING
# ===================================================

# ---------------- Unicode ----------------

print("Unicode")

num = "H"
print(ord(num))
print("The ord() function prints the unicode code point of a character")

code = " "
print(ord(code))

# ---------------- Indexing ----------------

print("Index")
print("Every character in a string has an index")

sher_coder = "Code with sheryains"

print("Here C has index 0 and -19")
print("Here o has index 1 and -18")
print("Here d has index 2 and -17")
print("Here e has index 3 and -16")
print("And so on")
print("Even spaces are included in indexing")

print("To print a specific index, here I used index 2")
print(sher_coder[2])

print("We can print more than one index like this")
print(sher_coder[3], sher_coder[6])

# ---------------- Slicing ----------------

print("String slicing")
print(sher_coder[10:14:1])
print("The code above slices out 'sher' from the variable sher_coder")

print("Format of slicing: variable[start index : end index : step]")
print("Note: the end index is EXCLUSIVE (not included), so use end+1 to include it")
print("If you don't specify a step, Python uses a default step of 1")

college = "college"
print("college")
print(college[::2])  # prints 'clee' - every 2nd character starting from index 0

print("If you don't specify a start or end, Python treats them as the full string")
print(college[::])
print("This prints the complete string since we gave no start, end, or step")
