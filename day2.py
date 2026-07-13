# a = 5
# b = "2"

# print("a" + b)   #answer = a2

# print("5" + b)  #answer = 52

# a = "7"   # Alt + Shift + down(Not click enter)
# a = 7
# b = "3"
# b = 3
# print(a + b)
# print(a + b)

# a = "7"
# b = "3"

# print(a + b)
# print(int(a) + int(b))

# Two type of typecasting
# 1. Explicit typecasting (Me work on this as programmer)
# 2. inplicit typecasting (Python work autometically)


# Explicit typecasting

# string = "15"
# number = 7
# string_number = int(string)

# this = string_number + number
# print("This is sum string and number :", this)

# -----------------------------

# a = 7.7
# b = 2.2

# print(a + b)
# print(a - b)

# -----------------------------

# Implicit typecasting 

# python automatically converted
# a to int
# a = 7
# print(type(a))

# # python automatically converted
# # b to float
# b = 7.7
# print(type(b))

# # python automatically convertes c to float as it is a float addition

# c = a + b
# print(c)
# print(type(c))
# print()
# print(dir(a))


# Taking User Input

# a = int(input("Enter the value : "))
# a = input()
# print("My name is:" , a)

# a = input("Enter your name :")
# print("My name is" , a)

# x = input("Enter first number :")
# y = input("Enter second number :")

# print(x + y)   # 1st num :- 12 , 2nd num :- 11 ,  Output is :1211
# The reason is i not defiend the (int), this reason the values are not added.

# x = int(input("Enter first number :"))
# y = int(input("Enter second number :"))

# x = input("Enter first number :")
# y = input("Enter second number :")

# print(x + y)   # 1st num :- 12 , 2nd num :- 11 ,  Output is :23
# print(int(x) + int(y))
# I defined the (int) and i entred the integer value , this reason the values are added.


# a = int(input("Enter first number :"))
# b = float(input("Enter second number :"))

# print("Addition :",a + b)
# print("Subtration :",a - b)
# print("Multiplication :",a * b)
# print("Division :",a / b)
# print("Floor division :",a // b)
# print("Module :",a % b)
# print("Power :",a ** b)


# String :
# Anything that you encolose between single or double quotation marks in considerd a string .

# name = "preet"
# name1 = "Tirth"

# apple = 'This is for you "the trip of dubai". '

# print("Hyy ," + name)
# print(apple)

# Multiline string 

# a = """This is for you,
# my name is preet patel,
# i study to data science."""

# a = ''' This is for you,
# my name is preet patel,
# i study to data science.'''

# b = "I am 18 year old,\n" \
# "And i completed deploma,"

# print(a)
# print()
# print(b)


# name = "Preet"   # Preet is sequance of charcater , it's started to (0).

# print(name[0])  #indexing 
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])  #error

# it's direct show the index number

# print(name.index("t"))
# print(name.index("P"))
# print(name.index("e"))
# print(name.index("e"))
# print(name.index("r"))


# Arrar is collection of items.

# Using looping

# name = "Preet"

# for character in name:
#     print(character)
