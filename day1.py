# repl's :- Read-evaluate-print loop

# print("Hello World")

# print(34 + 32)

# print(f"I am learning python")


# variable :- variable are store the data

# Data types :-   int , float , str , bool


# preet = 18
# b = preet
# print(b,"\n")
# print("\n")
# print(preet)

# a = 12
# b = 12

# a = int(input("Enter the value of A :"))
# b = int(input("Enter the value of B :"))
# print()
# print(f"Addition of A and B : {a + b} \nSubtraction of A and B : {a - b} \nDivision of A and B : {a / b} \nFloor division of A and B : {a // b} \nMultiplication of A and B : {a * b}")

# print(f"Subtraction of A and B : {a - b}")

# print(f"Division of A and B : {a / b}")
# print(f"Floor division of A and B : {a // b}")

# print(f"Multiplication of A and B : {a * b}")

# print(f"Module of A and B : {a % b}")


# a = 12
# b = 12

# print("The value of ", a , "+" , 12 , " is:" , a + b)   #addition
# print("The value of ", a , "-" , 12 , " is:" , a - b)   #subtraction
# print("The value of ", a , "*" , 12 , " is:" , a * b)   #multiplication
# print("The value of ", a , "/" , 12 , " is:" , a / b)    #division
# print("The value of ", a , "//" , 12 , " is:" , a // b)   #floor division
# print("The value of ", a , "%" , 12 , " is:" , a % b)      #module
# print("The value of ", a , "**" , 12 , " is:" , a ** b)   #power  /  Exponential


# ==============================
# SIMPLE CALCULATOR IN PYTHON
# ==============================

# ------------------------------------------------
# STEP 1 : TAKING INPUT FROM USER
# ------------------------------------------------

# 'num1' is a VARIABLE
# Variable ka kaam data store karna hota hai

# input() ek FUNCTION hai
# Ye user se value leta hai

# float() ek FUNCTION hai
# Ye input ko decimal number me convert karta hai

num1 = float(input("Enter first number: "))

# Dusra number store karne ke liye variable
num2 = float(input("Enter second number: "))

# ------------------------------------------------
# STEP 2 : OPERATOR INPUT
# ------------------------------------------------

# 'operator' ek VARIABLE hai
# Isme + - * / store hoga

operator = input("Enter operator (+, -, *, /): ")

# ------------------------------------------------
# STEP 3 : CONDITIONS
# ------------------------------------------------

# if ek CONDITIONAL STATEMENT hai
# Ye condition check karta hai

# == ek COMPARISON OPERATOR hai
# Equal check karta hai

if operator == "+":

    # result ek VARIABLE hai
    # + ek ARITHMETIC OPERATOR hai
    result = num1 + num2

    # print() FUNCTION output show karta hai
    print("Answer =", result)
    
# elif ka meaning:
# "else if"

elif operator == "-":

    # - subtraction operator
    result = num1 - num2

    print("Answer =", result)

elif operator == "*":
    # * multiplication operator
    result = num1 * num2

    print("Answer =", result)

elif operator == "/":
    # / division operator

    # Nested if condition
    # Zero division avoid karne ke liye
    if num2 != 0:
        # != means NOT EQUAL
        result = num1 / num2
        print("Answer =", result)
    else:
        # Agar second number 0 ho
        print("Cannot divide by zero")

# else tab chalega jab koi bhi condition true na ho
else:
    print("Invalid Operator")

