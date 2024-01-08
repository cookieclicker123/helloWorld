# lambda parameters: expression

#def double(x):
    #return x * 2

#print(double(5))

double = lambda x:x * 2
multiply = lambda x, y:x * y
add = lambda x, y, z: x + y + z
fullName = lambda firstName, lastName: f"{firstName} {lastName}"
ageCheck = lambda age: True if age >= 18 else False
print(ageCheck(12))
print(fullName("Bro", "Code"))
print(add(2, 4, 6))
print(multiply(2, 10))
print(double(5))


