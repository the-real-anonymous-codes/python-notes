"""INPUT"""
print("To take input from user we use input() function")

name = input("Enter your name: ")
print("value entered by user is always save as str")
print("To convert it into int , float , boolean we use int() , float() , and bool() function respectively")

age = int(input("Enter your age: "))
'''OUTPUT'''
print("There are two ways to give output") 
# 1st use one or more strings
print("Hi",name,"you are",age,"years old")

#2nd use f-string
print(f"Hi {name} you are {age} years old")

'''OPERATORS'''
# ARITHMETIC operators
# for maths calculations there are various operators in python given below
# + , - , * , / , // , ** , %
# operators even works for float value
a = 20
b = 10
c = 30
d = 10.5
# + i.e sum i.e addition
print(a+b+c) #prints 20 + 10 + 30 i.e 60

print(a+b+c+d) #print 20 + 10 + 30 + 10.5 i.e 70.5

# - i.e difference i.e subtraction 
print(a-b-c) #prints 20 - 10 -  30 i.e -20

print(a-b-c-d) #prints 20 - 10 - 30 - 10.5 i.e -30.5


# * i.e  multiply 
print(a*b*c) #prints 20 x 10 x 30 i.e 6000

print(a*b*c*d) #prints 20 x 10 x 30 * 10.5 i.e 63000


# / i.e division i.e divide 
print(a/b) #prints 20/10 i.e 2.0
print(c/d) #prints 30/10.5 i.e 2.857142857

# // i.e floor  division 
print(a//b) #prints int 20/10 i.e 2
print(c//d) #prints 30/10.5 i.e 2.0

# ** i.e exponent i.e power i.e index
print(a**b) #prints 20^10  i.e 10240000000000
print(c**d) #prints 30^10.5 i.e 3234246929812255.5

# % i.e modulus i.e remainder
print(a%b) #prints remainder of 20/10 i.e 0
print(c%d) #prints remainder of  30/10.5 i.e 9.0

'''
sequence
() : brackets
** : Exponent
* , / , // , %  : multiplication , division , floor division , modulus   (all at same level jo phele aaya)
+ , - : add , subtract '''
