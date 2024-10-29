
x = "Villan"

def my_fun():
    global x
    x = "Hero"
    print("Python is "+x)
my_fun()

def this_fun():
    print("X is a "+x)

this_fun()