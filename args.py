#       *args = paramater that will pack all arguments into a tuple
#        useful so that a function can accept a varying number of arguments

def add(*stuff):
    sum = 0
    #stuff[0] = 0 , this doesn't work as items in tuple are unchangeale, next line solves this prolem
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6))