# list comprehension = a way to create a new list with less syntax
#                     can mimic certain lambda functions, easier to read
#                     list = [expression (if/else) for item in iterable]

squares = []
for i in range(1, 11): 
    squares.append(i*i)
print(squares)

#same program using list comprehension

squares2 = [i*i for i in range(1, 11)]
print(squares2)

students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
#passedStudents = list(filter(lambda x: x >=60, students))
#print(passedStudents)

#same program using list comprehension

#passedStudents2 = [i for i in students if i >=60]
#print(passedStudents2)

passedStudents = [i if i >=60 else "FAILED" for i in students]
print(passedStudents)