# Enumerator used for to get index & data with pair 
fruits = ['apple','banana','kiwi','kiwi']

# creating new list & adding elements
list_fruits = [(index, fruit) for index, fruit in enumerate(fruits)]
print(type(list_fruits),list_fruits)

for index, fruit in enumerate(fruits):
    print(index,fruit)
    
# creating dic & adding new elements
dic_fruits = {index: fruit for index, fruit in enumerate(fruits)}
print(type(dic_fruits),dic_fruits)