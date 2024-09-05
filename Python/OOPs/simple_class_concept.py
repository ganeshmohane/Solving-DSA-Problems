# we name files in python in smaller case and connected by underscore i.e. my_function()
# functions also same way
# but classes are like PasaclConvention - first letter big and no space i.e. MyClass()

class MyClass:
    def __init__(self,name):
        self.name = name
    
    def HelloWorld(self):
        return f"Hello World,{self.name}"
    
o1 = MyClass("Ganesh")
print(o1.HelloWorld())