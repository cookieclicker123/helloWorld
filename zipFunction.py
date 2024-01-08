# zip(*iterables) = agregate elements from two or more iterables (list, tuples, sets, etc.)
# creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
loginDate = ["1/1/2021", "1/2/2021", "1/3/2021"]

users = zip(usernames, passwords, loginDate)




for i in users:
    print(i)