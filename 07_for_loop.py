# ===================================================
# FOR LOOP
# ===================================================

# If you have to print "Hello my sher" 100 times, you cannot write
# print("Hello my sher") 100 separate times.
# For this you can use loops - as the name suggests, they run in a loop.

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

# ---------------- break, continue & else ----------------

for b in range(0, 101, 1):
    if b == 10:
        break
    print(b)
# break immediately exits the loop, so this stops as soon as b reaches 10

for b in range(0, 101, 1):
    if b == 101:
        break
    print(b)
# break is looking for 101, but range(0, 101) only goes up to 100
# (the stop value is always exclusive) so this condition is never True,
# and break never triggers - the loop just runs to completion

for c in range(0, 101, 1):
    if c == 10:
        continue
    print(c)
# continue skips just that one iteration, so 10 is skipped but the loop keeps going

for c in range(0, 101, 1):
    if c == 232:
        continue
    print(c)
# continue is looking for 232, but our range only goes up to 100
# so this condition is never True, and every number prints normally

for c in range(0, 101, 1):
    if c % 2 != 0:
        continue
    print(c)
# continue skips every odd number, so only even numbers from 0 to 100 are printed

for c in range(0, 101, 1):
    if c % 2 == 0:
        continue
    print(c)
# continue skips every even number, so only odd numbers from 0 to 100 are printed

for e in range(0, 101, 1):
    if e == 20:
        break
    print(e)
else:
    print("This else won't run, because the loop was stopped early by break")
# the else block of a for loop only runs if the loop finishes WITHOUT hitting a break

for e in range(0, 101, 1):
    if e == 109:
        break
    print(e)
else:
    print("This else will run, because break was never triggered")
# since 109 never appears in range(0, 101), break never fires,
# so the loop finishes normally and the else block runs