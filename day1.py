# This is  a comment
# This also a comment

''' This is a Multiline comment. Python doesn't have multiline comment but we use 
docstring as multiline comment'''

# Variables

sher = "I am learning  python from NYC by sheryians "
print(sher)
print(type(sher))
print("Strings can store anything")
print("Name of variable  cannot start with number")
print("Spaces are not allowed in naming of variable")
print("Special chars are not allowed in naming of variable expect  underscore")

a = 23
b = -12
c = 629
print(type(a))
print(type(b))
print(type(c))
print("To check type we use type()")

x = 133.323
y =  233.4332
z = -24244/13412
v = 1232/1232
print(x)
print(y)
print(z)
print(v)
print(type(x))
print(type(y))
print(type(z))
print(type(v))

print("Anything number p/q from is a  float value")

u  = 4 + 9j
print(u)
print(type(u))

print("Here u is a complex")

K = True
N = False
print(K)
print(N)
print(type(K))
print(type(N))

print("True and False are boolean")
print("In True and False T and F  should be capital")

print("type conversion")

print("Unicode")
num = "H"
print(ord(num))

print("ord function prints uncode of string")

code = " "
print(ord(code))

print("Index")
print("Every char in string has a index")

sher_coder =  "Code with sheryains"

print("Here C has index 0 and -19")
print("Here o has index 1 and -18")
print("Here d has index 2 and -17")
print("Here e has index 3 and -16")
print("And so on")
print("Even spaces are also included in indexing")


print("To print specific index here i used 2")
print(sher_coder[2])

print("We can print more then one index like this")
print(sher_coder[3] , sher_coder[6]) 

print("String sciling")
print(sher_coder[10:14:1])

print("Above code slice sher from variable sher_coder")
print("Format of sciling              print(variable[start index : end index + 1 : steps ]")
print("If we dont enter step python will consider steps as  default which is 1")

college = 'college'
print("college")
print(college[::2]) #THIS WILL PRINT clee

print("If we don't enter start and end point while slicing python will consider it as default")

print(college[::])

print("This will print complete variable as we didn't enter start , end and step")


print("TYPE CONVERSION")
print("int() converts into integer")
print("str() converts into string")
print("float() converts into float")
print("bool() converts into boolean")

print("ANY VARIABLE CAN BE written in STRING USING str()")
print("But every variable cannot be written in int() and float()")
print("Every variable can be converted into a Boolean using bool()")

num = 23432.9378  #this is a float
print(int(num))  #this converts num into int i.e 23432
print(str(num)) #this converts num into a str i.e "23432.9378"
print(bool(num)) #this converts num into a bool  i.e True 

print("How to decide whether bool will print True or False")
print("if variable indicates  it will print False else it will print True")
print("for example")
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

print("NOTE for python 2.0 = 2 and 2345678.0 = 2345678")