# Slicing and opertion in string 

# length of string 
# we can find the length of string using len() function.

# name = "Preet Patel"
# print(len(name))

# print(name[0:5])

# name = "Mango"
# len1 = len(name)
# print("This is a", len1 , "Mango.")  #output :- 5
# print("This is a", len , "Mango.")  #output :- <built-in function len>

# name = "Mango"
# print(name[0:4])    #Mang
# print(name[:4])     #Mang
# print(name[1:5])    #ango
# print(name[:])      #Mango
# print(name[0:-2])   #Man
# print(name[0:-4])     #M
# print(name[-1:-4])   #NOt printed anything
# print(name[-4:-1])  #ang     

# [-4 : -1]  mango is 5 word 
# [5 - 4] = 1
# [5 - 1] = 4
# Mango
# [1 : 4] = ang   ==> Answer
# start 1 but stop 3 not stop in the 4 beacuse in the slicing you will always stop 1 step ago.

# nome = "Preetpatel"

# print(nome[-5:-1])

# [-5 : -1] preetpatel is 10 word 
# [10 - 5] = 5
# [10 - 1] = 9
# preetpatel
# [5 : 9] = pate  ==> this is a answer


# pie = "Applepie"

# print(pie[:5])
# print(pie[5:])
# print(pie[2:6])
# print(pie[-8:])  


# alphabets = "ABCDE"
# for i in alphabets:
#     # print(alphabets)
#     # print()
#     print(i)

# Upper in string 
# The upper() method is use to convert the all text in the upper case 

# The strings are immutable
# Upper and lower method ka jab use hota he to woh new string bana ta he purani string ko change nahi karta he 
# kyoki string is immutable.

# name = "Preet"

# print(name.upper())
# print(name.lower())

# day_14-06

# Using strip :- it's removed only the last value (!,@,#... etc).

# name = "Preet!!!"
# print(name.rstrip("!"))  #output :- Preet (rstrip are removed [!].)

# name = "!!!Preet!!!!!!"
# print(name.strip("!"))    #output :- !!!Preet

# name = "Tirth@@@@"
# print(name.rstrip("@"))

# name = "Om####"
# print(name.rstrip("#"))


# Replace :- method change The Any Value

# name = "Preet"
# print(name.replace("Preet" , "Data Science"))


# using split :- split is use to convert the value in the list form

# name = "Patel Preet"
# print(name.split())


# Using capitalize :- it's convert the text first letter into the capital nd another chacter convert in to the lower case.

# name = "preet PAtel"
# print(name.capitalize())   #output :- Preet patel


# center :- this is use for text to come in the center

# str1 = "Welcome to my computer program"
# print(str1.center(100))

# str1 = "Welcome to my computer program"
# print(len(str1))
# print(len(str1.center(100)))     #output : 30 and 100, (30 len is also str1 answer and 100 is i will given)

# str1 = "Welcome to my computer program"
# print(str1.center(100, "."))


# count() :- it's use to count the value which time it's return 

# name = "Preet are loving ai"
# print(name.count("a")) 


# endswith :- it's check the string check the string is end or not to specific letter / word 

# name = "Preet Patel !!!"

# print(name.endswith("!"))  #output : True 
# print(name.endswith("l"))   #output : False , because last letter is (!).

# name = "Welcome to the my python practice file"

# print(name.endswith("the" , 9, 14))   # output :- True (this is check the value is under the slicing)
# print(name.endswith('to' , 1 , 6))    # output :- False


# Find : this method are search value and return the index where i is present. if given value is absent from the string then return -1.

# str1 = "Hyy my name is preet patel , i am learned data science"

# print(str1.find("is"))    #output :- 12   (the first letter is [i] it's 12 number index)
# print(str1.find("ai"))      #output :- -1   (the reson is ai is not defined)


# index :- it's also serch a letter , but in the index value are not defined then in output are not execute the program. find are 
# excuted the program and gived the -1 , but index are giving the error.

# name = "Today is started python programming langauge"

# print(name.index("start"))   #output :- 9
# print(name.index("Preet"))   #output :- error


# isalnum :- it's check the value A-a,z-Z and 0-9 , not allowed the space , if you used the space your output is error 

# name = "Preetpatel18"
# print(name.isalnum())   #output :- true

# name1 = "Preet patel"
# print(name1.isalnum())  #output :- false (because is used the space)
# name2 = "Preet00"
# print(name2.isalnum())   #output :- false


# islower : check the values it's lower true or false 

# name = "preet patel"
# print(name.islower())


# isupper : check the values it's upper true or false 

# name = "PREET"
# print(name.isupper())


# isprintable : run only printable values not other values

# nae = "Kirtan is my class friend"
# print(nae.isprintable())

# nae = "Kirtan is my class friend\n"
# print(nae.isprintable())   #output :- false (becuase \n is not a printable value)


# isspace :- only return the space not any charcter

# name = "        "
# print(name.isspace())   #output :- true
# name = "preet"
# print(name.isspace())   #output :- false


# istitle :- it's check the all value's first letter if upper to answer is true , if lower answer is false

# name = "Preet Patel"
# print(name.istitle())     #output :- true
# name = "preet Patel"
# print(name.istitle())     #output :- false


# startswith : you willcheck the value to which word to start this.

# name = "Preet patel is a future data scientist"
# print(name.startswith("Preet"))     #true
# print(name.startswith("patel"))     #false


# swapcase :- convert the value in upper to lower case and lower to upper case

# name = "This Is Great Opportunity"
# print(name.swapcase())


# title : this is use to convert the all values in the title form ]

# name = "Today i will started learn a python"
# print(name.title())
