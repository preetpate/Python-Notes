# Variable

# PreetPatel = 1      #Pascal case

# preetPatel = "Tirth"      #camel case

# preet_patel = "Kartik"        #snake case

# val = "Four"  
# print(val)
# print()

# a = 12
# b = a
# print(type(a))
# print(b)

# a = "Preet "
# b = "Patel"
# print(a + b)

# a = "Patel "
# b = "Preet"
# print(a + b)

# Data Types

# 1 ==> Numbers

# Int , Float & complex

# a = 21       #Int
# b = 21.5     #float
# c = 12/3     # float    (/) is operator it's giving the result of float
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(a) , type(b), type(c)) 
# print()

# p = 18j     #complex in the complex use only (j) not use another keyword

# print(type(p))

# 2 ==> String 

# st = "My Name is Preet Patel"
# print(type(st))

# 3 ==> Boolean 

# p = True 
# t = False
# print(type(p) , type(t))


"""String"""

# The ASCII (American standard code for information interchange) it's a subset of Unicode 
# the ASCII first 128 unicode code points are same 
# print(ord('A'))      #65(Ascii and unicode)
# print(ord('Rupees symbol'))      #8377 (unicode only)

# a = "A"
# print(ord(a))      #65   this is unicode 
# print()
# b = 65
# print(chr(b))

# \uXXXX	Unicode escape (4 hex digits)	"\u20B9" → ₹
# \UXXXXXXXX	Unicode escape (8 hex digits)	"\U0001F60A" → 😊

# Indexing 
# 2 type of indexing 
# 1 foward indexing and 2 backward indexing 

# 1 farward indeing is starting for (0) 0,1,2,3 and it's count in starting value 
# 2 backward indexing is starting for (-1) -1,-2,-3  and it's count in last value 

# a = "Preet Patel"

# print(a[2])
# print(a[-2])

# slicing  

# print(a[0:8:1])
# print(a[-1 : -7 : -1])
# print(a[6:10], a[2])   # start the 6 to 9 beacuse it's - the one value 

# print(a[-4], a[-2])


# type conversion 
# explicit type conversion
# function ==>  int() , float() , str() , bool()

# a = 12
# print(type(a))

# a = 18
# print(type(a))
# a = str(a)
# print(type(a))
# print()
# b = "18"
# print(type(b))
# b = int(b)
# print(type(b))
# print()
# c = 14.4
# print(type(c))
# c = bool(c)
# print(type(c))
# print()
# d = True
# print(type(d))
# d = float(d)
# print(type(d))
# print()


# boolen 

# a = 18
# print(bool(a))       #true
# a = "Preet"
# print(bool(a))       #true
# b = -5
# print(bool(b))       #true
# print()

# there are 7 False value (false , 0 , 0.0 , " ", [ ] , { } , ( ))

# c = 0
# print(bool(c))      #false
# a = [ ]
# print(bool(a))      #false
# a = False 
# print(bool(a))      #false


# implicit type conversion 
# implicit type conversion woh automatic work karta he 

# a = 12
# print(12/3)   # 4.0    this is implicit type conversion   ==>  (/) operator is always come to float .

# explicit type conversion
# explicit type conversion woh manual work karna padta he 

# a = 12
# print(12//3)   #4   type int (//) is a floor division and it's a int.
# print(int(12/3))


# Input and Output

# Output
# you probalby know till now, how to provide the output of the code you have written and that is with print() function

# Input
# there is user and you want to ask the age of that user, how can you do so, it's easy using input()

# name = "Preet"
# age = "19"
# print(name , age)       # this is output (print) print ke allava koi tarike se output genrate nahi kar sakte 


# Input
# a = input("Enter you age :")      # me agar iss ko print na karu to output age likhne ka bhi option nahi aayega 
# print(a)


# Normal string 
# ex :-
# name = "Preet"
# age = 19
# print(name)
# print("My name is",name,"and age is",age)


# Formatted String (f-string)
# Variables ko string ke andar directly use karne ke liye.
# ex :-
# name = "Preet"
# age = 19
# print(f"My name is {name} and age is {age}")


# Raw String (r)
# Backslash (\) ko special character nahi maanta.
# ex :-
# price = r"Preet and Python"
# print(price)
# price1 = r"Preet\nPython"        #in the raw string not work (\n)
# print(price1)


# Multi-line String (Triple Quotes)
# ex :-
# text = """Hello
# Welcome to Python
# Learning"""
# print(text)

# practice :-
# 1) accepts the number from user.
# num =int(input("Enter your Number :"))

# 2) accage from user and print it.
# age = int(input("Enter your age :"))
# print(age)


# Operators 
# Operators are symbols that perform operations on variable and values.
# Types of operators : arithmatic operators , comparission operators , logical operators

# Arithmetic Operators
# + , - , * , / , // , ** , %

# a = 4
# b = 20

# sum = (a + b)
# print(sum)
# sub = (a - b)
# print(sub)
# mul = (a * b)
# print(mul)
# div = (a / b)
# div = (b / a)      # the answer is a 5.0 beacuse (/) is a float operator 
# print(div) 
# a = 4
# b = 22
# floor = (b // a)      # the answer is 5 beacuse the (//) is covent all value in the integer.
# print(floor)

# print(5**3)  
# print(20 % 3)

# print(12+4/2)      #the answer is 14.0


# assignment operator
# += , -= , *= , /= , //= , **= , %=

# a = 20    # assigment opertor ka use hota he ki value ko assign karna variable me eans variable banana and value add karna 

# compound assignment opertions

# a = 20
# print(a + 20)     # 40
# print(a + 20 + 40 + 60)    #140
# print(a - 20 + 30 + 10 * 2)    # 50


# a = 20
# a = 18
# print(a)    #the answer is 18 beacuse a = 18 is re-assign value 

# a = 18
# a = a + 18
# print(a)     # 36    re-assign

# this is a exampel
# a = 20
# a = a + 20     # yaha par new value assigin ki gai he that reason 20 + 20 is 40
# a = a + 40      #and yaha par a + 40 means 40 + 40 is 80
# a = a + 60      # 140
# a = a + (-15)     # 125
# print(a)      

# assignment operator 

# a = 18
# a += 20     # the answer is 38
# a += 12     # 50
# a -= 20     # 30
# a *= 2      # 60
# a /= 2      # 30.0
# a //= 2     # 30
# a **= 2        # 900
# print(a)


# camparison operator
# == , != , > , < , >= , <=

# a = 12
# b = 12

# print(a == b)   # true
# print(a != b)   #false
# print(a > b)    # false    # greater than
# print(a < b)    #false     # less than
# print(a >= b)   #true
# print(a <= b)    #true


# print(18 > 11)    # true 
# print(18 < 3)      # false


# ASCII (American  standard code for information interchange)

# print(ord("A"))    # 65
# print(ord("a"))    # 97
# print(chr(65))     # A
# print(chr(97))     # a

# print(ord("A"))    # 65
# print(ord("B"))     # 66
# print("A" > "B")    # false
# print("ABC" > "ABD")    # false
# print("ABC" < "BCD")   # true

# print("A" > "68")    # true   beacuse the compair the first value and 6 unicode is 54  that reason the answer come true 
# print("a" < "90")      # false 


# Logical operator
#  and , or , not 

# print(123 > 100 , 18 == 18)      # true true 

# And  :  this is use to if one value are false the answer is also false  : means 3 true he and 1 false the answer is false

# print(123 > 100 and 18 == 18)       # true    if both values are true that answer is true
# print(123 > 100 and 18 == 18 and 31 > 11)     # true

# print(123 > 100 and 18 == 31)        # false     if one value true and second value are false the answer is false
# means ek bhi value false hui to answer are aso false

# print(123 > 150 and 18 == 18 and 90 > 45 and 55 < 99)    #false also this is a break beacause first value are false the automatically 
#  answer is false 

# OR  :  this is use to if one value are true the answer is automatically true : means 3 false he and 1 true the answer is true

# print(123 > 179 or 18 == 31 or 111 < 111 or 111 == 111)       # true beacuse one value are true
# print(123 > 190 or 18 == 19 or 121 < 121  or 35 < 33)      # false beacause the every value are false 

# Not  :  this is convert the value if value is true that answer is false and the value is false that answer is true

# print(not 18 == 18)      # false 
# print(not 18 < 11)      # true

# Practice quiestion 

# print(126 > 130)      # false
# print(18 == 18)      # true

# print((456 == 456)  != (235 == 236))     # true 
# print((333 == 333) != (111 == 111))      # false
# print((121 <= 121) != (121 <= 121))      # false

# print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13)     # true
# print(181 < 111 or 321 == 123 or 66 > 69 or 22 != 22)       # false
# print(12 < 13 and 44 == 44 and 55 > 44 and 123 <= 123)     # true
# print(123 < 124 and 45 == 45 and 21 > 12 and 123 != 123)     # false

# print(12 < 11 or 18 == 18 and 18 <= 18)      # true
# print(12 < 11 or 18 == 18 and 18 < 18)      # false

# print(True and bool(0))    # false
# print(True and bool(1))     # true
# print(True or bool(0))    # true 


# conditional statements 
# conditional statement in python allow decision-making by executing diffrent blocks of code based on condition.

# types of conditional statements 
# if 
# if-else 
# if-elif-else

# If
# a = 18
# if a > 10:
#     print("I will complete task")      # I will complete task 

# a = 15
# if a < 21:
#     print("What is if condition")

# If-else
# money = int(input("Enter your number :-"))

# if money == 10 :
#     print("I will buying Mango douly")
# else :
#     print("I will not buy anything")

# if-elif-else
 
# money = int(input("Enter the amount:- "))

# if money < 10:
#     print("I will not buy anything.")
# elif money == 10:
#     print("I will buy Mango Dolly Ice Cream.")
# elif money <= 50:
#     print("I will buy Choco Bar.")
# else:
#     print("I will buy Faluda.")


# practice questions

# this is greater than / less than

# a = int(input("Enter your value of A :-"))
# b = int(input("Enter your value of B :-"))
# if a < b:
#     print("B is greater than A")
# else :
#     print("A is greater than B")

# a = int(input("Enter your value of A :-"))
# b = int(input("Enter your value of B :-"))
# if a < b:
#     print(f"{b} is greater than {a}")
# elif(b < a):
#     print(f"{a} is greater than {b}")
# else:
#     print(f"The both value are same")

# numbers = int(input("Enter your numbers :-"))
# if numbers <= 10 :
#     print("This value's are low")
# else :
#     print("This value's are high")


# this is gender sir/mam

# gen = input("Please tell me your gender M and F form :-").upper()        # if you not use upper that use logical operator
# if gen == 'M' or gen == "m":
#     print("Good Morning Sir")
# elif gen == "F" or gen == "f":      # i using (OR) beacuse if one condition are true that output comes are also true
#     print("Good Morning Mam")          # if i will used (AND) operator that output comes are enter only M or F
# else : 
#     print("Please enter only M or F")

# gender = input("Your techer is :-")
# if gender == "male":
#     print("Good Morning Sir")
# else :
#     print("Good Morning Mam")


# This is odd/even 

# i = int(input("Enter your number :-"))

# if (i%2== 0):
#     print("This number is even")
# else :
#     print("This number is odd")


# this is a name and age prgram for voter id 

# name = input("Tell me your name :-")
# age = int(input("Enter your age :-"))
# if age >= 18 :
#     print(f"{name} You are valid for the voter")
# else :
#     print(f'{name} Your are not valid for the voter')
# remaning_years = 18 - age
# print(f"You come for vote after {remaning_years}.")


# check the leap year or not 

# year = int(input("Enter the year :-"))
# if year %100 == 0 and year %400 == 0:      #100 yeh 1st century year tha, agar 100 se divsible he to 400 se bhi hona chahiye  
#     print("It's a leap year")
# elif year %100 != 0 and year %4 == 0:      # 4 iss liye liya he kyoki agar 100 se divisible nahi he to kya 4 se he ya nahi
#     print("Its a leap year")
# else :
#     print("It's a normal year") 

# year = int(input("Enter the year :-"))
# if year % 400 == 0:
#     print("This year is Leap year")
# elif year % 4 == 0 and year % 100 != 0:
#     print("This is also leap year")
# else :
#     print("This is not leap year")


# If elif ladder
# taking the temperacture in celsius

# t = int(input("Enter the temprature :-"))
# if t < 0:
#     print("Feezing cold")
# elif t >= 0 and t < 10:
#     print("Very cold")
# elif t >= 10 and t < 20:
#     print("cold")
# elif t >= 20 and t < 30:
#     print("pleasant")
# elif t >= 30 and t < 40:
#     print("Hot")
# else : 
#     print("It's very Hot")


# Loops in python
# Loops in python allows us to execute a block of code multiple times without rewriting it.

# types of loop
# For loop :- it's work on numbers, kisi range ke basis pe
# while loop :- yeh work karta he condition ke basis par , agar condition true chal rahi he to kam chalta rahega and
# false huvi to wahi par kaam ruk jayega 

# Range function
# (start , stop , step)

# a = range(1 ,20 ,2)     # using range

# for i in a :       # i is a veraible 
#     print(i)        # the answer is 1 ,3 ,5.......19

# without range

# for i in range(1 ,20 ,3):
#     print(i)

# for i in range(20):     # 0,1,2,3,4.........19
#     print(i)

# for i in range(16 , 0 , -1):      # agar aapko reverse jana he stop par aapko -1 value leni hogi means nagitive value
#     print(i)

# for i in range(-3 ,-16, -1):
#     print(i)

# for i in range(5 ,51 ,5):
#     print(i)


# Aapne hisab se deside karna he ki konsa table bana na he to 

# n = int(input("Enter who you want the table :-"))
# for i in range(n , (n*10)+1, n):
#     print(i)


# loops in string using index value

# a = "Preet Patel"
# for i in range(9):
#     print(a[i])
# print()

# a = "Preet Patel"
# for i in a[: 9 : 2]:
#     print(i)


# if print the value using the index value 

# a = "Preet is learning python"
# print(len(a))        # length are always come to count to the 1 and range count for 0.

# for i in range(len(a)):
#     print(a[i])


# iterating directly over the string 

# a = "Preet patel is learning python"

# for i in a:
#     print(i)


# Break continue else

# for i in range(1,21):
#     if i == 15:
#         break          # else aap nahi lgaoge fir bhi chalega
#     else:
#         print(i)

# for i in range(26):
#     if i == 19:
#         break       # agar break chala to else nahi chalega and break nahi chala to else chalega
#     else :
#         print(i)


# Continue
 
# for i in range(1,21):
#     if i == 15:     # 15 woh run nahi hoga. continue 15 ko redirect karega iss liye jo bhi value doge woh pront nahi hogi usko skip kar dega
#         continue
#     else:                  # else aap nahi lgaoge fir bhi chalega
#         print(i)

# for i in range(35):
#     if i == 25:
#         continue
#     print(i)

# for i in range(1,21):
#     if i == 21:
#         print("The exicute a code")
#         break
#     print(i)
# else:
#     print("The value's are not exicuted")        # agar menhe value 21 ya 21 se jayada ki li hogi to not exicute aa jayega 
# and break statment work nahi karega 

# for i in range(1,21):
#     if i == 15:
#         print("The exicute a code")
#         continue
#     print(i)
# else:

#     print("The value's are not exicuted")    # 14 ko exicute kar dega continue and baki value ko run karega


# practice question

# Accept an integer and print hello world n times.

# n = int(input("Please tell your me your number :-"))
# for i in range(n):
#     print("Hello Preet")

# n = int(input("Enter your number :-"))
# for i in range(n):
#     print(i)          # enter the number is 5 that answer is 0,1,2,3,4

# n = int(input("Enter your number :-"))
# for i in range(n)
#     print(i + 1)      # enter the number is 5 that answer is 1,2,3,4,5 , kyoki range 0 se start hota he and hamne i + 1 kiya iss liye 1 se start kiya

# print natural number up to n.

# n = int(input("Enter your number :-"))
# for i in range(1, n+1):
#     print(i)

# n = int(input("Enter the your number :-"))
# for i in range(n):
#     print(i)

# Reverse for loop. print n to 1.

# n = int(input("Enter your number :-"))
# for i in range(n , 0 , -1):
#     print(i)

# for i in range(18, 0 , -1):
#     print(i)

# for i in range(-4 , -10 , -1):
#     print(i)

# n = int(input("Enter your number :-"))
# for i in range(n , -7 , -1):
#     print(i)

# take a number as input and print the table 

# n = int(input("Tell me your table :-"))
# for i in range(n , (n*10)+1 , n):
#     print(i)

# n = int(input("tell your table :-"))
# for i in range(1,11):
#     print(n ,"*", i, "=",n*i)
#     print()
    # print(f"{n} + {i} = {n * i}")


# n = int(input("Enret the number :-"))
# for i in range(n + 1):
#     print(i)     # enter the 5, answer is 0,1,2,3,4,5

# n = int(input("Enret the number :-"))
# for i in range(n + 1):
#     print(i + 1)     # enter 5 , answer is 1,2,3,4,5,6

# n = int(input("Enret the number :-"))
# for i in range(n):
#     print(i + 1)   # enter 5 , answer is 1,2,3,4,5

# sum of the n term

# sum = 0
# sum = sum + 1     # 1
# sum = sum + 2     # 3
# sum += 3          # 6
# sum += 4          # 10
# sum += 5          # 15
# sum = sum + 6     # 21
# print(sum)

# i using the for loop for sum the n numbers.

# n = int(input("Enter the number of sum :-"))
# sum = 0
# for i in range(1 , n+1):
#     sum = sum + i
# print(f"your sum is : {sum}")        # agar aapko direct answer chahliye to space mat do

# n = int(input("Enter the number of sum :-"))
# sum = 0
# for i in range(1 , n+1):
#     sum = sum + i
#     print(f"my sum is : {sum}")        # agar aapko line bt line answer chahiye to space do

# n = int(input("Enter the number of substraction :-"))
# sub = 100
# for i in range(1 , n+1):
#     sub = sub - i
#     print(sub)

# n = int(input("Enter the number of multiplication :-"))
# mul = 1
# for i in range(1 , n+1):
#     mul = mul * i
#     print(mul)       

# n = int(input("Enter the number if division :-"))
# div = 50
# for i in range(1 , n+1):
#     div = div / i
#     print(div)

# Factorial a number

# n = int(input("Enter the factorial number :-"))
# fact = 1
# for i in range(1 , n+1):
#     fact = fact * i
#     print(f"Your factorial is : {fact}")


# Agar aapko sirf perticular value tak even ya odd number chaliye to yeh program use kar sakte ho

# n = int(input("Enter your number :-"))
# for i in range(1, n+1):
#     if i%2 == 0:
#         print(i)      # enter the 10 , answer is 2,4,6,8,10

# n = int(input("Enter your number :-"))
# for i in range(1, n+1):
#     if i%2 == 1:
#         print(i)    # enter 10 , answer is 1,3,5,7,9

# sum of the odd and even number in a range separatly

# n = int(input("Enter your number :-"))
# even = 0
# odd = 0
# for i in range(1, n+1):
#     if i%2 == 0:
#         even = even + i
#     else :
#         odd = odd + i
#     print(f"Your sum of even is : {even} and odd is : {odd}")    # you seen the manually answer

# n = int(input("Enter your number :-"))
# even = 0
# odd = 0
# for i in range(1, n+1):
#     if i%2 == 0:
#         even = even + i
#     else :
#         odd = odd + i 
# print(f"Your sum of even is : {even} and odd is : {odd}")     # you seen the direct answer 

# print all the factors of a number.

# n = int(input("Enter the number :-"))
# for i in range(1 , n+1):
#     if n%i == 0:             # iss me agar me (i) ki jagah (1) likhuga and enter 10 maruga to answer 1,2,3,4.....10 aayega 
#         print(i)             # but (i) karke 10 enter karunga to answer 1,2,5,10 aayega
# jis bhi value ke sirf 2 factor aa rahe he woh prime value he jiske multiple factors aa raha he woh composite he

# accept a number and check if it a perfact number or not a number whose sum of factors is equal to the number itself
# Ex :- 6 = 1, 2, 3 = 6

# n = int(input("Enter your number is perfact or not :-"))
# sum = 0
# for i in range(1 ,n):      # perfact number he ya nahi woh dekhne ke liye hamne n+1 nahi kiya he sirf n likha he 
#     if n%i == 0:
#         sum = sum + i
# if sum == n:
#     print("This number is perfact number")
# else :
#     print("It's not perfact number")

# check the weather number is prime or not.

# n = int(input("Check this is prime number or not :-"))
# count = 0
# for i in range(1 , n+1):
#     if n%i == 0:
#         count = count + 1
# if count == 2:
#     print("This is a prime number")
# else :
#     print("it's not a prime number")

# n = int(input("Enter the number is prime or not :-"))
# prime = 0
# for i in range(1 ,n):
#     if n%i == 0:
#         prime = prime + 1
# if prime == 1:
#     print("This is a prime numbers")
# else :
#     print("not a prime")

# reverse a string without using building a function

# a = "Prret Patel"
# print(a[::-1])

# a = input("Enter your name :-")
# print(a[::-1])

# using loop
# a = input("Enter your name :-")
# reverse = " "
# for i in a:
#     reverse = i + reverse     # i + reverseiss liye kiya he ki reverse ho sake agar me reverse + i karunga to name jesa tha wehsa hi print hoga
# print(reverse)

# # using indexing
# a = input("Enter the name :-")
# b = " "
# for i in range(len(a)-1,-1,-1):      #-1 woh 3 baar iss liye likhe hekyoki woh range he start,stop,step
#     b = b + a[i]            # agar only i likho ge to sirf number print hoge and a[i] karoge to name print hoga
# print(b)

# check string is pallindrome or not.

# a = input("Enter the pallindrome name :-")
# b = ""        # agar space doge iss me to correct answer nahi aayega
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# if b == a:
#     print("Your string is pallindrome")
# else :
#     print("Not pallindorme")


# print(dir(str))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
#  '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
#  '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
#  '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
#  'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 
# 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 
# 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 
# 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'] 


# count all letter, digits and special symbols from a given string 
# given : str1 = "P@#$%^&!@4"
# Expected outcome :
# total counts of chars, digits and symbols
# chars = 8
# digits = 3
# sysmbol = 4

# a = "pdfpreet1234@#$%^&*"
# char = 0
# dig = 0
# spchr = 0

# for i in a:
#     if i.isdigit():
#         dig += 1
#     elif i.isalpha():
#         char += 1
#     else :
#         spchr += 1
# print(f"Your digits are : {dig}\n your alphabets are : {char}\n your special charcters are : {spchr}")


# While loops
# the while loop repeats a block of code as long as a condition is true. it is useful when the number of iterations is unknown before execution

# a = 1
# while a <= 30:
#     print(a)
#     a = a + 1           # yeh a = a + 1 iss liye diya he kyoki value 1 1 karke + hoti rahe 30 tak 
# first time meri a ki value 1 he second time mera loop iterate karega tab value + 1 hogi means 2 ho jayegi 

# a = int(input("Enter the number :-"))
# b = 1
# while b <= a:
#     print(b)
#     b = b + 1

# Print the unlimited name

# a = input("Enter the name :-")
# b = int(input("Enter the number :-"))
# count = 1
# while count <= b:
#     print(a)
#     count = count + 1

# Print the unlimited name and number

# a = input("Enter the name :-")
# b = int(input("Enter the number :-"))
# count = 1
# while count <= b:
#     print(count , a)
#     count = count + 1

# practice question

# print 1 to 10

# a = 1
# while a <=10:
#     print(a)
#     a = a + 1

# print 10 to 1

# a = 10
# while a >= 1:
#     print(a)
#     a = a - 1

# a = int(input("Enter the number :-"))
# b = 1
# while a >= b:
#     print(a)
#     a = a -1 

# check the even or odd

# a = int(input("Enter the number :-"))
# b = 1
# while b <= 1:
#     if a%2 == 0:
#         print("It's a even number ")
#     else :
#         print("odd number")
    # b = b + 1

# print even number

# a = int(input("Enter the number :-"))
# b = 1
# while b <= a:
#     if b%2 == 0:
#         print(b)
#     b += 1

# print th odd number 

# a = int(input("Enter the number :-"))
# b = 1
# while b <= a:
#     if b%2 == 1:
#         print(b)
#     b = b + 1

# print the multiplication table 

# n = int(input("Enter the table :-"))
# a = 1
# while a <= 10:     # agar 10 ki jagah n likho ge to koi table print karo uss number tak hi print hoga, means 5 ka table print karoge to 
#     print(f"{n} * {a} = {n * a}")        # 5 * 5 = 25 tak hi table print hoga uske aage nahi jayega kyoki n me number ko hum select karte he  
#     a += 1

# saperate each digit of a number and print it on the new 

# a = 256
# while a > 0:     # a > 0 jab tak (a) ki value 0 se badi he tab tak process karte jao  , our abhi 256 0 se badi he to process start hogi 6 nikal jayega 
#     print(a % 10)   # uske baad woh a me jayega , baad me a ki value re-assign hogi firse value ke pass jayega value bachi he 25 ese karke process 0 hogi
#     a = a // 10     # jab value 0 ho jayegi loop stop ho jayegi kyoki 0 se badi value nahi di gai he 
#  a = a // 10 se me aapne loop ko rokunga nad (a % 10) uski help se me aapni last ke value ko extrac karunga

# a = int(input("Enter the number :-"))
# while a > 0:
#     print(a % 10)
#     a = a // 10   # yeh iss liye use hota he taki value n number tak print na ho (.) ke baad ki value ko remove karne ke liye use karte he 
# agar tum (//) ki jagah (%) use karoge to multile number print ho jayenge

# Accept a number and print its revers

# a = int(input("Enter your number :-"))
# rev = 0
# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10
# print(rev)

# Accept a number and check if it  is a pallindromic number (if number and its reverse and equal)

# a = int(input("Enter the number :-"))
# copy = a   # iss me copy name variable iss liye bana gya kyoki , agar a ki value change ho jaye, fir bhi copy variable me orignal store rahe
# rev = 0

# while a > 0:
#     rev = rev * 10 + a % 10   # iss me kya hoga ki value revese karnge to a ki value change ho jayegi, iss ki wajah se copy variable create kiya gya he 
#     a = a //10

# if copy == rev :
#     print("It's a pallindromic number ")
# else :
#     print("Not pallindromic number")

# Create a random number guessing game with python.

# import random

# num = random.randint(1,10)
# tries = 0

# while True:
#     guess = int(input("Gusse the number 1 to 10 :-"))
    
#     if guess == num:
#         tries += 1
#         print("You are a right guess in", tries ,"tries")
#         break

#     elif num < guess:
#         tries += 1
#         print("Go to the little lower value")

#     elif num > guess:
#         tries += 1
#         print("Go the littel Upper")

#     else :
#         tries += 1
#         print("Not right")


# only 5 chaces avalible in this game , and 5 se jayada chance liye to game over
# import random

# num = random.randint(1,10)
# tries = 0
# print('You have only 5 chance')

# while True:
#     guess = int(input("Gusse the number 1 to 10 :-"))
    
#     if guess == num:
#         tries += 1
#         print("You are a right guess in", tries ,"tries")
#         break

#     elif tries == 4:    # iss me 4 iss liye diya he kyoki menhe tries ki value 0 di iss liya me yaha par jitni value dunga 1 jayada print hogi
#         print('Sorry, your 5 chances is over')
#         print('Game is over')
#         break

#     elif num < guess:
#         tries += 1
#         remaining = 5 - tries
#         print("Remaining Chances :", remaining)
#         print("Go to the little lower value")

#     elif num > guess:
#         tries += 1
#         remaining = 5 - tries
#         print("Remaining Chances :", remaining)
#         print("Go the littel Upper")

#     else :
#         tries += 1
#         print("Not right")


# Functions
# A function is a reusable block of code that performs a specific task. It executes only when it is called.
# There are many in-build function in python like print(), input(), len() etc.

# print(dir(print))
# ['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
#  '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__name__',
#    '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__',
#      '__str__', '__subclasshook__', '__text_signature__']

# import builtins
# import inspect
# for name in dir(builtins):
#     obj = getattr(builtins, name)
#     if inspect.isbuiltin(obj):
#         print(name)

# __build_class__
# __import__
# abs ,aiter ,all ,anext ,any ,ascii ,bin ,breakpoint ,callable ,chr ,compile ,delattr ,dir ,divmod ,eval ,
# exec ,format ,getattr ,globals ,hasattr ,hash ,hex ,id ,input ,isinstance ,issubclass ,iter ,len ,locals ,max ,min 
# next ,oct ,open ,ord ,pow ,print ,repr ,round ,setattr ,sorted ,sum, vars

# def hello():
#     print("This my first function")
# hello()

# def guess():
#     print("This is a function name guess")
#     guess = 19
#     print(guess)
# guess()

# def use():
#     i = int(input("Enter the number :-"))
#     if i%2 == 0:
#         print("This is even number ")
#     else :
#         print('odd number')
# use()

# def user():
#     a = input("Enter your name :-")
#     b = int(input("Enter your age :-"))
#     print(f"{a} your age is : {b}")
# user()


# This is check the your year, create this program using functions

# def birthday_program():
#     from datetime import date

#     name = input("Enter your name :-")
#     birth_day = int(input("Enter your birth_date(1-31) :-"))
#     birth_month = int(input("Enter the your birth_date_month(1-12) :-"))
#     birth_year = int(input("Enter your birth year :-"))
#     print()
#     current_day = int(input("Enter the current date :-")) 
#     current_month = int(input("Enter the current month :-"))
#     current_year = int(input("Enter the current year :-"))

#     birth_date = date(birth_year, birth_month, birth_day)
#     current = date(current_year, current_month, current_day)

#     age = current_year - birth_year

#     if (current_month, current_day) < (birth_month, birth_day):
#         age -= 1

#     total_days = (current - birth_date).days
#     next_birthday = date(current_year, birth_month, birth_day)

#     if next_birthday < current:
#         next_birthday = date(current_year + 1, birth_month, birth_day) 

#     days_left = (next_birthday - current).days

#     print("\n========== RESULT ==========")
#     print("Your Age :", age, "Years")
#     print("Total Days Lived :", total_days)
#     if days_left == 0:
#         print(" Happy Birthdayyy ")
#     else:
#         print(f"{days_left} : Days Left For Your Birthday ")
#     print("============================")

# birthday_program()

# Function in parameter and argument
# parameter 
# Parameter is a variable that receives the value when the function is called.
# argument
# Argument is the actual value passed to the function when it is called.

# def sum(a , b):
#     print(f"Sum of the number is : {a + b}")
# sum(12,12)

# def sub(a , b):
#     print(f"Substraction of a and b is : {a - b}")
# sub(18 , 12)
# sub(77 , 55)
# sub(121 , 111)

# def great(name):
#     print(f"Your name is : {name}")
# great("Preet")


# Types of arguments :- positional argument, default argument , keyword argument

# positional argument
# def add(a,b):
#     return a + b
# print(add(3,5))

# keyword argument
# def introdunction(name , age):    # age,name is keyword
#     print(f'your name is {name} and age is {age}')
# introdunction("Preet" , 19)
# introdunction(age = 19, name = "Preet")    # age = 19 is keyword argument
# introdunction(19 , "Preet")    # yaha par pahele age print hogi and badme name print hoga, iss liye define karna important he 

# default argument

# def sum(a , b = 18):     # b = 18 is default argument
#     print(f"The sum is {a + b}")
# sum(18)
# sum(18 , 20)    # 20 is replace value


# def greet(name = "Patel"):
#     print(f"Name is {name}")
# greet()     # is me patel print hoga
# greet("Preet")    # iss me preet print hoga 

# practice

# def pallindrome(st):
#     st = str(st)
#     rev = ""
#     for i in range(len(st)-1,-1,-1):
#         rev = rev + st[i]

#     if rev == st:
#         print(f'{st} is a pallindrome')
#     else :
#         print(f'{st} is not pallindrome')

# pallindrome("NAMAN")
# pallindrome("TIRTH")
# pallindrome(1331)
# pallindrome(1212)
# pallindrome("MALAYALAM")
# pallindrome(input("Enter the pallindrome name :-"))
# pallindrome(int(input("Enter the pallindrome number :-")))

# Return 

# def hello() :
#     return "My name is preet patel"   # return yeh karega ki aapni value ko return kar dega function me jaha se aap call kar rahe ho
# print(hello())

# def pallindrome(st):
#     st = str(st)
#     rev = ""
#     for i in range(len(st)-1,-1,-1):
#         rev = rev + st[i]

#     if rev == st:
#         return f'{st} is a pallindrome'
#     else :
#         return f'{st} is not pallindrome'

# print(pallindrome("NAMAN"))
# print(pallindrome("TIRTH"))
# print(pallindrome(1331))
# print(pallindrome(1212))
# print(pallindrome("MALAYALAM"))
# print(pallindrome(input("Enter the pallindrome name :-")))
# print(pallindrome(int(input("Enter the pallindrome number :-"))))


# In build data structures
# data structures are used to store, organize and manipulate data effciently. python provides several built-in data structure
# 4 type of in build data structure :- List , Tuple , Dictionary , Set

# Custom data structures 
# now there are some custom data structures as well like Stack , Queue , Linked List , Graph etc.
# And arounf these data structure there are some algorithms like seraching algorithm , sorting algorithm.

# list

# a = [12,13,14,15.5,16,print() , True]
# print(a[1])
# print(a[1:7:2])
# print(a[-1])
# print(a[6:1:-1])
# print(a[-1:-6:-1])

# a[5] = "Preet"
# print(a)
# a[2] = 18
# print(a)

# a.pop()
# print(a)
# a.pop(3)
# print(a)

# List traversing and methods
# now list travesing is also similar to string travesing it can be looped using the index value and directly

# 1st way using index
# a = [12,13,14,15,16,17.6]

# for i in range(len(a)):
#     print(a[i])

# 2nd way directly on values
# a = [12,13,14,15,16,17.6]
# for i in a:
#     print(i)     # iss me agar aap value ko access kar rahe ho to index ko access nahi kar sakte

# Some methods you will get if what they are used 

# print(dir(list))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', 
# '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__',
#  '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
#    '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 
#    'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# help(list)

# append
# a = [1,2,4,5,6,7]
# a.append(18.5)
# a.append(12)
# a.append(-5)
# print(a)

# insert
# a = [1,2,3,4,5]
# a.insert(3,18)
# a.insert(2,21)
# a.insert(1,51)
# a.insert(4,27)
# print(a)

# extend
# a = [1,2,3,4,5]
# a.extend([5])
# a.extend("Preet")   #'p'.'r','e','e','t'
# a.extend(['Preet'])   # 'preet'
# a.extend(['Tirth'])
# print(a)

# remove
# a = [1,2,3,2,4,5]
# a.remove(5)
# a.remove(2)   #1,3,2,4   yeh starting se remove karega value ko 
# a.remove(4)
# print(a)

# remove and store
# a = [1,2,3,4,5]
# remove = a.pop(2)  
# print(remove)    # 3
# print(a)   #1,2,4,5
# remove = a.pop(4)
# print(remove)    # 5
# print(a)    #1,2,3,4

# index with variable 
# a = [1,2,3,4,5]
# index = a.index(2)   # 1
# index = a.index(3)   # 2
# print(index)
# print(a)

# count numbers
# a = [1,2,3,4,5,2,2,2,1,3,4,5,3,6,5,4,3,2]
# count = a.count(2)    # 5
# count = a.count(4)    # 3
# print(count)

# number sort 
# a = [1,3,2,4,7,5,3,5,2,9]
# a.sort()
# print(a)
# b = [1,2,4,3,6,5,4,3,2,2,6,8,9,7,5,8,7,9,0]
# b.sort()
# print(b)
# c = [1,3,2,4,7,5,3,5,2,9]
# c.sort(reverse = True)
# print(c)
# d = [1,2,4,3,6,5,4,3,2,2,6,8,9,7,5,8,7,9,0]
# d.sort(reverse= True)
# print(d)

# reverse number 
# a = [1,4,2,6,3,2,6,4,9,8,9,7,5,6,7,5,3]
# a.reverse()
# print(a)
# b = [5,4,7,6,1,3,2,4,9,7,6,4,7,5,7]
# b.reverse()
# print(b)

# copy numbers 
# a = [1,2,3,6,5,4,3,7,5,6,3,4,2]
# copy = a.copy()    # yeh list ka data copy karta he print karte he uska duplicate value ko print karta he , original and duplicat are different
# print(copy)   # the value are same but copy is duplicate

# clear 
# a = [1,2,3,4,5,6,7,8,9]
# a.clear()
# print(a)

# some practice 

# l = [1,2,3,4,5]
# l[0] = 11
# print(l)    # 11,2,3,4

# print positive and nagitive element in list 

# l = [-11,21,13,18,-55,-44,58]
# print("This is a possitive value's :")
# for i in l:
#     if i >= 0:
#         print(i)
# print("It's a nagative value's :") 
# for i in l:
#     if i <= -1:
#         print(i)

# Using range function

# a = [-1,-2,2,4,3,5,-6,-4]
# print("This is a positive value :")
# for i in range(len(a)):
#     if a[i] >= 0:
#         print(a[i])
# print("Nagative value :")
# for i in range(len(a)):
#     if a[i] <= -1:
#         print(a[i])


# l = [-11,21,13,18,-55,-44,58]
# for i in l:
#     if i >= 0:
#         print(f"Possitive value's are :- {i}")
#     else :
#         print(f'Its nagative value :- {i}')

# mean of list elements 

# a = [11,22,33,44,55,66,77,88]
# sum = 0
# for i in a:
#     sum = sum + i
# print(sum/len(a))

# a = [1,2,3,4,5,6,7]
# sum = 0
# for i in range(len(a)):
#     sum = sum + a[i]
# print(sum/len(a))    # sum = 28, mean = 4.0
# print(sum//len(a))   # floar = 4

# Find the greatest element and print index too

# a = [11,13,16,21,12,31,22,27]
# largest = a[0]
# index = 0
# for i in range(len(a)):
#     if a[i] > largest:    
#         largest = a[i]   #a[i] ke under value aa rahi he
#         index = i     # i ke under index aa rahi he 
# print(f"Your largest number is :- {largest} and index is {index}")

# Find the second greatest element 

l = [21,13,22,10,17,33]
largest = l[0]
sec_largest = l[0]
for i in l:
    if i > largest:     # i ki value largest se badi honi chahiye , jiski value jyada hogi to uske pahele wali value second lagrgest value ho jayegi
        sec_largest = largest    # to woh yaha par aayegi , and second largest value = largest value
        largest = i    # and wahi largest value = i de diya he 
print(f"{sec_largest} is a second largest value")
print(f"{largest} is a largest value")