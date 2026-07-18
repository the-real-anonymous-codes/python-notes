# ===================================================
# LOOPS - for & while
# ===================================================

# If you have to print "Hello my sher" 100 times, you cannot write
# print("Hello my sher") 100 separate times.
# For this you can use loops - as the name suggests, they run in a loop.

# There are two types of loops in python:
# 1st For loop
# 2nd While loop

# ---------------- For Loop ----------------

# If you want to run something "n" number of times, where "n" is a
# non-negative integer, you use a for loop.

for i in range(5):
    print("Hello my sher", i)

# range(5) generates the numbers 0, 1, 2, 3, 4 - so the loop runs 5 times

# ---------------- While Loop ----------------

# If you want to run something until a condition becomes False, and you
# don't know in advance when the condition will become False, you use a
# while loop.

count = 0
while count < 5:
    print("Hello my sher", count)
    count += 1

# The loop keeps running as long as "count < 5" is True,
# and stops as soon as it becomes False
