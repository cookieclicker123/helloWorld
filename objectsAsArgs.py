class Car:
    colour = None

class Motorcycle:
    colour = None

def changeColour(vehicle, colour):
    vehicle.colour = colour


car1 = Car()
car2 = Car()
car3 = Car()

bike1 = Motorcycle()


changeColour(car1, "red")
changeColour(car2, "white")
changeColour(car3, "blue")
changeColour(bike1, "black")


print(car1.colour)
print(car2.colour)
print(car3.colour)
print(bike1.colour)