# ===================================================
# CONDITIONAL STATEMENTS - if, elif, else
# ===================================================

# To check conditions we use if, elif, and else
# We need to create an indented block after the condition, followed by a colon (:)

# Example: checking whether a user is a valid voter

age = int(input("Enter your age: "))

if age >= 18:
    print("You are a valid voter")
else:
    print("You are not a valid voter")
    print(f"You have to wait {18 - age} years to vote")

# This checks whether the user is a valid voter based on their age.
# In if-else, 1st priority is given to if, and else is the last priority.
# If the condition for 'if' is True, that block runs.
# Any condition that is False for 'if' is automatically treated as True for 'else'.

# Suppose in the program above the user enters a negative age -
# it would be False for 'if' but True for 'else', which is misleading.
# To fix this we can add an elif block.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are a valid voter")
elif age < 0:
    print("Please enter a valid age")
else:
    print("You are not a valid voter")
    print(f"You have to wait {18 - age} years to vote")

# You can chain as many conditions as needed using if-elif.
# You can also combine multiple conditions in a single if/elif block using 'or' or 'and'.

# For more projects on if-elif-else, visit my repo on GitHub:
# github.com/sirvilalit/if-elif-else-practice
