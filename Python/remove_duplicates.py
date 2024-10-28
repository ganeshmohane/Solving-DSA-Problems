def remove_duplicates():
    a = ['a','b','a','a','b','c']
    b = list(dict.fromkeys(a))
    print(b)

remove_duplicates()