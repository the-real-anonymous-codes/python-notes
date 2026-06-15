# This is  a comment
# This also a comment

''' This is a Multiline comment. Python doesn't have multiline comment but we use 
docstring as multiline comment'''

# Variables

sher = "I am learning  python from NYC by sheryians "
print(sher)
print(type(sher))
# strings can store anything
 # name of variable  cannot start with number
 # spaces are not allowed in naming of variable
 # Special chars are not allowed in naming of variable expect  underscore

a = 23
b = -12
c = 629
print(type(a))
print(type(b))
print(type(c))
# to check type we use type()

x = 133.323
y =  233.4332
z = -24244/13412
v = 1232/1232
print(type(x))
print(type(y))
print(type(z))
print(type(v))

# Anything number p/q from is a  float value

u  = 4 + 9j
print(type(u))

# Here u is a complex

K = True
N = False
print(type(K))
print(type(N))

# True and False are boolean
# in true and False T and F  should be capital

# type conversion

# Unicode
num = "H"
print(ord(num))

 # ord function prints uncode of string

code = " "
print(ord(code))

 # Index
 #Every char in string has a index

sher_coder =  "Code with sheryains"

 #Here C has index 0 and -19
 # o has 1 and -18
 # d has 2 and -17
 # e has 3 and -16
 # and so on

 # Even spaces are also included in indexing

print(sher_coder[2]) #To print specific index here i used 2
print(sher_coder[3] , sher_coder[6]) # we can print more then one index like this
# string sciling
print(sher_coder[10:14:1])
# above code slice sher from variable sher_coder
# format of sciling              print(variable[start index : end index + 1 : steps ]
# if we dont enter step python will consider steps as  default which is 1
college = 'college'
print(college[::2]) #THIS WILL PRINT clee
# If we don't enter start and end point while slicing python will consider it as default

print(college[::])
# This will print complete variable as we didn't enter start , end and step


# TYPE CONVERSION
# int() converts into integer
# str() converts into string
# float() converts into float
# bool() converts into boolean

# ANY VARIABLE CAN BE written in STRING USING str()
# but every variable cannot be written in int() and float()
# Every variable can be converted into a Boolean using bool()

num = 23432.9378  #this is a float
print(int(num))  #this converts num into int i.e 23432
print(str(num)) #this converts num into a str i.e "23432.9378"
print(bool(num)) #this converts num into a bool  i.e True 

# How to decide whether bool will print True or False 
# if variable indicates  it will print False else it will print True
# for example
a = ""
b = 0 
c =  "d"
d = 0.00
e = "0"
print(bool(a)) #False
print(bool(b)) #False
print(bool(c)) #True
print(bool(d))  #False
print(bool(e)) #False

