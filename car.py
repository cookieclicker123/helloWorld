class Car:
    
    # Class variables
    wheels = 4
    doors = 2
    #like a defualt value within the class byut outside the constructor


    def __init__(self, make, model, year, colour):
        self.make = make #instance variable
        self.model = model #instance variable
        self.year = year #instance variable
        self.colour = colour #instance variable
    
    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" has stopped")
    
