# Animal base class
class Animal:
    def move(self):
        print("The animal moves...")

class Dog(Animal):
    def move(self):
        print("The dog runs! 🐕")

class Fish(Animal):
    def move(self):
        print("The fish swims! 🐠")

# Vehicle base class
class Vehicle:
    def move(self):
        print("The vehicle moves...")

class Car(Vehicle):
    def move(self):
        print("The car drives on the road! 🚗")

class Plane(Vehicle):
    def move(self):
        print("The plane flies in the sky! ✈️")


# Testing polymorphism with animals
animals = [Dog(), Fish()]
for animal in animals:
    animal.move()

# Testing polymorphism with vehicles
vehicles = [Car(), Plane()]
for vehicle in vehicles:
    vehicle.move()
