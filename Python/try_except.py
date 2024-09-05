# finally  - always runs despite others
# try - we add our usual code in it 
# except - if something error happens in try code then except shows it
# raise - raises errors like TypeError, NameError or simple Exception

# why used this - code clarity, effieciney , closing connections(finally)


def Division(x,y):
    try:
        result = x/y
    except:
        raise ZeroDivisionError("Cannot divide by zero")
    else:
        print(result)
    finally:
        print("Code Completed")
Division(1,1)
Division(1,0)

# try:
#     x = -1
#     if not type(x) is str:
#         raise TypeError("Type should be string")
#     if x  < 0:
#         raise Exception("No number less than 0")
# except NameError:
#     print("Name not defined")
# else:
#     print("No name error")
# finally:
#     print("Finally always runs")
    
    