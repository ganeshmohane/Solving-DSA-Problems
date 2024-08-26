# stack is a data structure which has only one opening, we can push,pop
# Its follows FILO : First In Last Out

def stack():
    arr = []
    choice = int(input("Enter the Choice : 1.Push, 2.Pop"))
    print(choice)
    if choice == 1:
        print(arr)
        num = input("Enter the no.")
        arr.append(num)
        stack()
    if choice == 2:
        print(arr)
        num = input("Enter the no. to remove ")
        arr.remove(num)
        stack()
    if choice not in range(1,2):
        exit() 
    print(arr)
stack()