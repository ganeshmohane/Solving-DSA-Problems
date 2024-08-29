# stack is a data structure which has only one opening, we can push,pop
# Its follows FILO : First In Last Out

#||
#||
#||
#--

def stack():
    arr = []
    while True:
        choice = int(input("Enter the Choice : 1.Push, 2.Pop\n"))
        print("Your Choice :",choice)
        if choice == 1:
            num = input("Enter the No. to add in the stack:")
            for i in num:
                # arr.insert(0,i)
                print(i)
                #arr.append(i)
            print(arr)
        elif choice == 2:
            print(arr)
            num = input("Enter the no. to remove ")
            arr.remove(num)
            print(arr)
        else:
            exit() 

stack()