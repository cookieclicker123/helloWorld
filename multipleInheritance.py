class Prey:
    
    def flee(self):
        print("The animal flees.")

    
class Predator:

    def hunt(self):
        print("The animal is hunting.")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
