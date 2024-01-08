class Animal:

    alive = True
    
    def eat(self):
        print("This animal is eating")

    def slumber(self):
        print("This animal is sleeping")
    
class Rabit(Animal):

    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    
    def fly(self):
        print("This hawk is flying")

rabbit = Rabit()
fish = Fish()
hawk = Hawk()

#print(rabbit.alive)
#fish.eat()
#hawk.slumber()

rabbit.run()
fish.swim()
hawk.fly()