"""
How Do You Define a Class?
"""

class Employee:
    def __init__(self, name, age):
        self.name =  name
        self.age = age

class Dog:
    
        # Class Attribute
        # Define class attributes directly beneath the first line 
        # of the Class Name
    species = "Canis familiaris"

        # Init Dunder Methods
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # Print Dunder Methods
    def __str__(self):
        return f"{self.name} is {self.age} years old"

        # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    
        # Instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage:,} miles"

"""
How Do You Instantiate a Class?
"""

miles = Dog("Miles", 4)
buddy = Dog("Buddy", 9)

print("Miles Name:", miles.name)
print("Miles Age:",miles.age)

print("Buddy Name:",buddy.name)
print("Buddy Age:",buddy.age)

print(buddy.species)

buddy.age = 10
print(buddy.age)

miles.species = "Felis silvestris"
print(miles.species)

print(miles.description())
print(miles.speak("Woof Woof"))

print(miles)

blue_car = Car(color="blue", mileage=20_000)
red_car = Car(color="red", mileage=30_000)

for car in (blue_car, red_car):
    print(car)

"""
How Do You Inherit From Another Class
"""

class Parent:
    hair_color = "brown"

class Child(Parent):
    hair_color = "purple"

class Parent:
    speaks = ["English"]

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.speaks.append("German")

# Child Classes from Parent Class Dog

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print("miles.species: ",miles.species)
print("buddy.name: ",buddy.name)
print("print(jack): ",jack)
print("jim.speak('Woof'): ",jim.speak("Woof"))

print('type(miles) =', type(miles))

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

miles = JackRussellTerrier("Miles", 4)   
print("miles.speak()",miles.speak()) 

miles.speak("Grrr")
print('miles.speak("Grrr")',miles.speak("Grrr")) 


