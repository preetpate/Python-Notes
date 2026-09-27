from pathlib import Path

def readfilefolder():
    path = Path('')          # abhi aap jis folder me ho usko exist karne ka kam karta he yah empty space
    items = list(path.rglob('*'))
    for i , items in enumerate(items):  # kisi bi list me aapki pass index hota he our values hoti he , in dono ko alg alg save karna chahte ho toh enumerate function ka use karte he 
        print(f"{i+1} : {items}")


def cretefile():
    try:         #using exception handling
        readfilefolder()    # samne wale user ko dikha sake , ki kya kya value excest karti he      
        name = input("Enter your file name :-")
        p = Path(name)
        if not p.exists(): 
            with open(p,"w") as fs:
                data = input("What you want to write in this file :-")
                fs.write(data)

            print("File created successfully")
        else :
            print('this file already exist')

    except Exception as err:
        print("An error eccured as {err}")

def readfile():
    try:
        readfilefolder()
        name = input("which file you want to read : ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:      #'r' is default mode , kuchh nahi likhoge fir bhi 'r' aayega
                data = fs.read()
                print(data)

            print("Readed successfully")
        else :
            print("The file doen't exist")
    except Exception as err:
        print(f"An error occured as {err}")


def updatefile():
    readfilefolder()
    name = input("tell which file you want to update :")
    p = Path(name)
    if p.exists() and p.is_file():
        print("press 1 for changing the name of your file :-")
        print("Press 2 for overwriting  the data of your file")
        print("press 3 for appending some content in your file")

        res = int(input("tell your response :-"))

        if res == 1:
            name2 = input('tell your file name :-')
            p2 = Path(name2)
            p.rename(p2)
            


print("prees 1 for creating a file")
print("prees 2 for reading a file")
print("prees 3 for updating a file")    
print("prees 4 for deleting a file")

check = int(input("Please tell your response :-"))

if check == 1:
    cretefile()

if check == 2:
    readfile()

# if check == 3:
#     updatefile() 