from pathlib import Path

def readfilefolder():
    path = Path(' ')          # abhi aap jis folder me ho usko exist karne ka kam karta he yah empty space
    items = list(path.rglob('*'))
    for i , items in enumerate(items):
        print(f"{i+1} : {items}")


def cretefile():
    readfilefolder()

print("prees 1 for creating a file")
print("prees 2 for reading a file")
print("prees 3 for updating a file")
print("prees 4 for deleting a file")

check = int(input("Please tell your response :-"))

if check == 1:
    cretefile()