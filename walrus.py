# walrus operator  :=
# := is an assignment operator
# := is used to assign values to variables as part of a larger expression

# The walrus operator is a new feature in Python 3.8

#happy = True
#print(happy)

#print(happy := True)

#foods = list()
#while True:
#    food = input("What food do you like?: ")
#    if food == "quit":
#        break
#    foods.append(food)
#print(foods)

#same code with walrus operator:

foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)  

print(foods)
    
