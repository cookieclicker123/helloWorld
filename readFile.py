try:
    with open("/Users/seb/Desktop/myTest.txt.rtf") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")  