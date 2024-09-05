# Polymorphism - Many Forms : using same methods name to handle different types of objects, enabling different behaviours
''' 
Below I have created Animal parent class and Dog and Cat are 
'''
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
class Dog(Animal):    
    def make_sound(self):
        print(self.sound)
class Cat(Animal):    
    def make_sound(self):
        print(self.sound)

dog = Dog("Dog","Boh")
cat = Dog("Cat","Meow")
dog.make_sound()
cat.make_sound()