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