class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    
    def shout(self):
        return f"{self.name} is {self.sound}ing!"

obj = Animal("Cat","Meow")
print(obj.shout())
