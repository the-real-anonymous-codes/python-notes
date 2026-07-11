print("Comparison operators")

print(" (== , > , < ,>= , <= , !=) ") 
# equal to , greater than , less than , greater or equal , less or equal , not equal
# comparison operators always gives bool  value as output

print(12==13) #False
print(12>14) #False
print(145 < 23456789) #True
print(120 <= 120) #True
print(1234 >= 1) #True
print(12 != 12) #False
print(22 != 21) #True

print("Logical operators")
print("and , or , not") 

print("If any condition is False 'and' operator prints False")

print((2==2) and (9 != 9)) #Here one condition is True and one is False and operator "and" is used so it will print False 
print((3 > 22) and (788 <= 789) and (334 == 344)) #Here one condition is False and two conditions are True and operator 'and is used  so it will print False
print((2==2) or (0 < 343) or (23>=22)) #Here all conditions are True and operator "and" is used so it will print True

print("If any condition is True 'or' operator prints True")

print((2==2) or (9 != 9)) #Here one condition is True and one is False and operator "or" is used so it will print True
print((3 > 22) or (788 <= 789) or (334 == 344)) #Here one condition is False and two conditions are True and operator 'or' is used  so it will print True
print((2==3) or (0> 343) or (23<=22)) #Here all conditions are False and operator "or" is used so it will print False

print("Not flips True into False and  False into True")

'''CONDITIONAL STATEMENTS'''


# if ,elif  , else
# To check conditions we use if , else and elif 

# we need to create a indent block after putting conditions with a : (colon) 

# example if we have to check  whether user is a valid voter or not

age = int(input("Enter your age: "))

if age >=  18 :
    print('You are a valid voter')
else :
    print("You are not a valid voter")
    print(f"You have to wait {18 - age} years to vote ")

# this checks whether user is a valid voter or not  by their age
# in if else 1st poritry is given to if and  else as last priotry
# if has a condition if it is  True then it will run accordingly 
# all conditions which are False for if will always True for else 

# Lets suppose in above program user enters a negative value it will become False for if but True for else 
# to fix these will can use elif block
age = int(input("Enter your age: "))
if age >=  18 :
    print('You are a valid voter')
elif age < 0 :
    print("please enter a valid age")
else :
    print("You are not a valid voter")
    print(f"You have to wait {18 - age} years to vote ")


# you can enter as much conditions using if - elif 
# you can also enter as much conditions in a if or elif block using 'or'  or  'and' operators

'''' for more projects on if elif else visit my repo on github https://github.com/sirvilalit/if-elif-else-practice '''