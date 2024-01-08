from car import Car

car_1 = Car("Chevy", "Corvette", 2021, "Blue")
car_2 = Car("Ford", "Mustang", 2022, "Red")

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.colour)
print()
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.colour)
print()
Car.wheels = 2
#car_1.drive()
#car_2.stop()

#car_1.wheels = 2

#print(car_1.wheels)

#print(car_2.wheels)

print(car_1.wheels)
print(car_2.wheels)

