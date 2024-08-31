# What is OOPs - It is the programming approach that models real-world entities as objects, 
# These objects have properties(data) & behaviours(methods).
# Objects = Instance of class, represents realworld entity
# Class = Blueprint for objects. 
# instance means copy of class

# for example 
'''
- car is class which has blueprint to create car objects.
- carname,model,color,year this are properties/data of objects.
- start, accelerate, brake, stop this are the methods used by objects
'''

class Car:
    def __init__(self,car,color,model,year):
        self.car = car
        self.color = color
        self.model = model
        self.year = year
        print(self.car,self.color,self.year,self.model)

    def start(self):
        print("Starting Car",self.car)
    def accelerate(self):
        print("Accelrating ",self.car)
    def brake(self):
        print("Braking",self.car)
    def stop(self):
        print("Stoping",self.car)

instance = Car("BMW","Red","S1",2024)
instance.start()
instance.accelerate()
instance.brake()
instance.stop()

# we use self for instance for reference like if we make instance ex. 'instance' then that self refers to that instance like it adds like instance.car = car like that
# also in methods we dont have to say add self to parameter we can directly use it