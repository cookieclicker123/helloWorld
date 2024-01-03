while True:
    name = input("Enter your name: ")
    if name != "":
        break

phoneNumber = "123-456-7890"

for i in phoneNumber:
    if i == "-":
        continue
    print(i, end="")

print("")

for i  in range(1,21):
    if i == 13:
        pass
    else:
        print(i)