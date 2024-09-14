''' *args : allows function to take any number of positional arguments
    **kwargs : allows function to take any number of keyworded positional arguments. '''

#we can replace args and kwargs with any word just put * in front of them and done
def order_pizza(flavour,*toppings,**details):
    print(f'Order recieved : \nflavour-{flavour},\ntoppings-{toppings},\nother details-{details}')

order_pizza('Cheese','masala','sauce',payment='cash',tip=50)