#sort method - used with lists
#sort function - used with iterables

#students = ('squidward', 'sandy', 'patrick', 'spongebob', 'mrkrabs')
#students.sort(reverse=True)

#sortedStudents = sorted(students, reverse=True)

#for i in sortedStudents:
#    print(i)

students = (("squidward", "F", 90), 
            ("sandy", "A", 95), 
            ("patrick", "C", 70), 
            ("spongebob", "B", 80), 
            ("mrkrabs", "D", 65))

age = lambda ages: ages[2]
#students.sort(key=age)
sortedStudents = sorted(students, key=age)

for i in sortedStudents:
    print(i)





