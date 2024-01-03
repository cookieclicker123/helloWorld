name = "bro" #global scope variable

def displayName():
    name = "Code" #local scope variable
    print(name)

displayName()
print(name)
