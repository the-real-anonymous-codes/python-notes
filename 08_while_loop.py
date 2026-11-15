# ===================================================
# WHILE LOOP
# ===================================================

# A while loop keeps executing as long as a condition is True.
# It is useful when the number of iterations depends on a condition,
# not a fixed count like in a for loop.

# Syntax:
# while condition:
#     statement

# Example 1: print numbers from 0 to 10

count = 0
while count <= 10:
    print(count)
    count += 1

# The loop stops when count becomes 11.

# Example 2: print the first 5 multiples of 3

num = 1
while num <= 5:
    print(3 * num)
    num += 1

# Example 3: use input with while loop

user_input = ""
while user_input.lower() != "exit":
    user_input = input("Type 'exit' to stop: ")
    if user_input.lower() != "exit":
        print(f"You typed: {user_input}")

# break, continue, and else in a while loop

# break exits the loop immediately

counter = 0
while counter < 10:
    if counter == 5:
        break
    print(counter)
    counter += 1

# continue skips the current iteration and moves to the next one

counter = 0
while counter < 10:
    counter += 1
    if counter % 2 == 0:
        continue
    print(counter)

# else runs when the loop finishes without hitting break

number = 0
while number < 5:
    print(number)
    number += 1
else:
    print("Loop finished normally without break.")

# A while loop can run forever if the condition never becomes False.
# Example:
# while True:
#     print("This will run forever")

# Important: always update the loop variable inside the loop,
# otherwise the condition may never change and the loop may become infinite.

