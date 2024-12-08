# we set current item and find min element from unsorted array
def find_min(arr,n,i):
    min_i = i
    for j in range(i+1,n):
        print(arr[min_i],arr[j])
        if arr[min_i] > arr[j]:
            min_i = j
        
    return min_i
        #pass

def selection_sort(arr,n):
    for i in range(0,n):
        min_i = find_min(arr,n,i)
        print(min_i,arr[i])
        if arr[i] > arr[min_i]:
            arr[i],arr[min_i] = arr[min_i],arr[i]
    return arr

arr = [2,6,1,4,9,0,2]
n = len(arr)
print(selection_sort(arr,n))