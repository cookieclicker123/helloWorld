import os

source = "folder"
destination = "/Users/seb/Desktop/folder"

try:
    if os.path.exists(destination):
        print("There is alrrady a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")

except FileNotFoundError:
    print(source +" was not found ")


