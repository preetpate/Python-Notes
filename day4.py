# if else statement

#   (=) is not a conditional opertor

# conditional opertor
# > , < , <=, >= , == , !=

# a = int(input("Enter your age :"))
# print("Your are is : ", a)

# if(a > 18):
#     print("You can drive the car")
# else :
#     print("You cannot drive the car")

# print(a > 18)
# print(a < 18)
# print(a <= 18)
# print(a >= 18)
# print(a == 18)
# print(a != 18)

# apple = 200
# budget = 200

# if (apple <= budget):           #if i not use <= , use only < to the answer is (you are not buy this). use any one ex:- [>= , ==] not use !=.
#     print("You buy this apple rs 200")
# else :
#     print("You are not buy this ")


# elif statement

# apple = 150
# budget = 200

# if (budget - apple > 200):
#     print("You are saving the more money")
# elif(budget - apple > 100):
#     print("You are  saving good money")
# elif(budget - apple > 50):
#     print("You are not good saving the money")
# else:
#     print("Current time your lost")

# num = int(input("Enter your number :"))

# if(num < 0):
#     print("Number is nagative")
# elif(num == 0):
#     print("The number is zero")
# else:
#     print("This is a positive")


# nested if statement

# num = int(input("Enter your number :"))

# if(num < 0):
#     print("Number is nagative")
# elif(num > 0):
#     # print("the number is positve")
#     if (num <= 10):
#         print("number is betwwen the 1 -10")
#     elif( num >= 10 and num <= 20):
#         print("Between the number 11 -20")
#     else :
#         print("number is grater than 20")
# else :
#     print("Number is zero")


# in this code are error 

# marks = int(input("Enter your marks : "))

# if(90 < marks):
#     print("Passing A grad")
# elif(80 < marks):
#     print("Passing B grad")
#     if(70 < marks):
#         print("Passing B2 grad")
#     elif(60 < marks):
#         print("Passing C grad")
#     else :
#         print("Passing D grad")
# else :
#     print("You are fail")


# Nested loop program
# marks = int(input("Enter your marks : "))

# if marks >= 33:
#     print("You are pass")
#     if marks > 90:
#         print("Passing A grade")
#     elif marks > 80:
#         print("Passing B grade")
#     elif marks > 70:
#         print("Passing B2 grade")
#     elif marks > 60:
#         print("Passing C grade")
#     else:
#         print("Passing D grade")
# else:
#     print("You are fail")


# if elif program
# marks = int(input("Enter your marks : "))

# if marks > 90:
#     print("Passing A grade")
# elif marks > 80:
#     print("Passing B grade")
# elif marks > 70:
#     print("Passing B2 grade")
# elif marks > 60:
#     print("Passing C grade")
# elif marks >= 33:
#     print("Passing D grade")
# else:
#     print("You are fail")


# import time

# timepass = time.strftime('%H:%M:%S')
# print(timepass)
# timepass = time.strftime('%H')
# print(timepass)
# timepass = time.strftime('%M')
# print(timepass)
# timepass = time.strftime('%S')
# print(timepass)

# import time

# hour = int(time.strftime('%H'))
# print("Current Hour:", hour)
# if hour >= 5 and hour < 12:
#     print("Good Morning")
# elif hour >= 12 and hour < 17:
#     print("Good Afternoon")
# elif hour >= 17 and hour < 21:
#     print("Good Evening")
# else:
#     print("Good Night")


# Day 16-05

# match case statement 
# syntax
# match vriable_name :
    # case 'pattern1' : // statement 1
    # case 'pattern2' : // statement 2
    # ...
    # case 'pattern n' : // statement n


# x = int(input("Ente th value of X :"))

# match x:
#     case 0:
#         print("X is zero")

#     case 4 if x % 2 == 0:
#         print("case is 4 ")

#     case _ if x < 10:
#         print("x is < 10")

#     case _ :
#         print(x)


# x = int(input("Ente th value of X :"))

# match x:
#     case 0:
#         print("X is zero")
#     case 4 :
#         print("Case is 4")

#     case _ if x!= 90:
#         print(x ," is not 90")
#     case _ if x!= 80:
#         print(x ," is not 80")

#     case _ :
#         print(x)


# Loops in python

# For loop can iterate over a sequence of iterable objects in python.

# name = "Preet"

# for i in name:
#     print(i)
#     # print(i , end=" ")
#     if(i == "r"):
#         print("This is for start coding")

# colors = ['red' , 'blue' , 'green' , 'white']

# for i in colors:
#     print(i)
#     for j in i:
#         print(j)

# colors = ['red', 'blue', 'green', 'white']

# for i in colors:
#     print(i, "has", len(i), "letters")


# range : make sequance of value 
# range = start , stop , step

# for i in range(5):
#     print(i)   #answer :- 0,1,2,3,4

# for i in range(5):
#     print(i + 1)   #answer :- 1,2,3,4,5

# for i in range(1 ,5):
#     print(i)      #answer :- 1,2,3,4

# for i in range(1 , 10 , 2):
#     print(i)     #answer :- 1 ,3 ,5 ,7 9

# for i in range(1 , 20 , 5 ):
#     print(i)

# for j in range(3):
#     print(j)

# while loop : - while loops execute statements while the condition is true.

# i = 0
# while(i < 3):
#     print(i)
#     i = i + 1

# i = int(input("Enter your number :"))
# while(i < 35):
    # i = int(input("Enter your 2nd number :"))      # agar isko comment kar du , and upper 50 se kam value likhu to unlimite value print hoga
#     print(i)
# print("Your loop are finish")

# interpreter , jab tak condition true hogi woh chalti rahegi woh exicute nahi hogi
# means ki vlaue 50 se chhoti he woh chalti rahe gi and 50 ya 50 + ho jayegi woh direct exicute ho jayegi

# i = 0
# while(i < 50):
#     i = int(input("Enter your number :"))     
#     print(i)
# print("Your loop are finish")


# decrement while loop

# count = 5
# while(count > 0):
#     print(count)
#     count = count - 1    # incase + 1 karu to unlimited value aayegi


# else with while loop

# x = int(input("Enter your number :"))
# while(x > 0):
#     print(x)
#     x = x - 1
# else :
#     print("counter is 0")


# Break statement  :- the break statement eneble a program to skip over a part of the code.

# The tables

# for i in range(1 ,11):
    # print("5 *" , i , "=" , 5 * i)
    # print("5 *" , i , "=" , 5 + 1)
    # print(f"6 * {i} = {6 * i}")

# for i in range(12):
#     if(i == 10):
#         break
#     print(f"5 * {i + 1} = {5 * (i + 1)}")

# print("Exicute the my loop")       #answer :- 5 ,10 , 15,........... 50   (stoped the 50 becuase it's break in the 9th value
# and i + 1 means going the 50)

# for i in range(16):
#     # print(f"6 * {i + 1} = {6 * (i + 1)}")
#     print("6 *" , i + 1 , "=" , 6 *(i + 1))
#     if(i == 10):   
#         break       # break the loop

# print("Exicute the my loop")        #answer :- 6 ,12 ,18 , 24, ......... 60 , 66   ( this is stop in the 66, because i first print 
# and later the if and break , i stoped the value in the 10 and i are + )


# for i in range(1 ,12):
#     if(i == 10):
#         print("Skip the itreation")
#         continue       # skip the itreation
#     print("5 *" , i  , "=" , 6 * i)

# for i in range(1, 101 ,1):
#     print(i , end=" ")
#     if(i == 50):
#         break
#     else :
#         print("Preet")
# print("This is e end")

# for i in [1,2,3,4,5,6,7,8,9,0]:
#     if(i%2 != 0):
#         continue

#     print(i)    #output :- 2,4,6,8,0    / if use i == 0 then output is :- 1,3,5,7,9


# do while loop example

# i = int(input("Enter your number :"))

# while True:
#     print(i)
#     i = i + 1
#     if(i % 100 == 0):
#         break

# while True:
#     num = int(input("Enter your number :"))
#     print(num)
#     if not num > 0:
#         break