# Sort array in decreasing 
def simple_sort():
    arr = [10,67,4,87,90,1]
    i = 0
    while True : # Outer while loop depends on swapped falg, if its false then it get existed
        swapped = False
        i = 0
        print(i,'outer')
        while i+1 < len(arr):
            print(i)
            if arr[i] < arr[i+1]:
                arr[i],arr[i+1] = arr[i+1], arr[i]
                swapped = True
            i +=1
        if not swapped :
            break
    return arr
sorted_arr = simple_sort()
print(sorted_arr)

# first i = 0 
# we are checking if i is less than next i? if yes then swap them and make i = 0 
# else move ahead
