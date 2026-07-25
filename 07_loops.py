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
# range() is the function most commonly used with a for loop.
# Syntax for range is range(start, stop + 1, step)
 
for k in range(0, 11, 1):
    print(k)
# prints 0 to 10 (stop is 11, but the end index is always exclusive)
 
for j in range(5, 51, 5):
    print(j)
# prints 5, 10, 15 ... 50 (multiples of 5 up to 50)
 
n = int(input("Please enter your number: "))
for m in range(n, (n * 10) + 1, n):
    print(m)
# prints the first 10 multiples of n, i.e. the table of n
 
a = "Python"
for i in a:
    print(i)
# a for loop can also iterate directly over a string, character by character
 
for i in range(len(a)):
    print(i)
# prints the index of every character in the string
 
for i in range(len(a)):
    print(f"{i} : {a[i]}")
# combining both - prints the index along with the character at that index
 
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