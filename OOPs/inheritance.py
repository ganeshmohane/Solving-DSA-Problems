# Inheritance is the one of the concept in OOP - Object Oriented Programming
# there are two classes parent-child or base-derived
# all methods are inherited to another class

class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def show(self):
        return f"Your name is {self.fname} {self.lname}"

    def say_loudly(self):
        return f"broooooo"
        
class Student(Person):
    pass
    
# obj = Person("Ganesh","Mohane")
obj = Student("Ganesh","Mohane")
print(obj.show())
print(obj.say_loudly())