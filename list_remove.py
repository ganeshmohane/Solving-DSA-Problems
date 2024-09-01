items = ['A','B','C','D','E']
new_items = []

for item in items:
    print(item,'from items')
    if item != 'B':
        new_items.append(item)
    print(new_items)  
