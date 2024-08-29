# Create Patterns

def pattern_one(n):
    for i in range(1,n+1):
        print(i*'*')

def pattern_two(n):
    for i in range(1,n+1):
        print(n*'*')
        n -= 1

def pattern_three(n):
    for i in range(1,n+1):
        n -= 1
        if i >= 1: a = i*'*'
        else: a = ''
        print(n*" "+i*'*')
        # for j in range(i,i+1):
            #print(a+j*'*'+(i*'*'))
            

n = int(input("Enter the No. :\n"))
# pattern_one(n)
# pattern_two(n)
pattern_three(n)

    # for i in range(1,n+1):
    #     n -= 1
    #     if i >= 1: a = i*'*'
    #     else: a = ''
    #     print(n*" "+i*'*'+a)