#parameter that will p[ack all arguments into a dictionary
def hello(**names):
    #print("Hello " + kwargs["first"] + " " + kwargs["last"])
    print("Hello", end=" ")
    for key,value in names.items():
        print(value, end=" ")
    print()

hello(title="Mr",first="Bro",middle = "dude", last="code")