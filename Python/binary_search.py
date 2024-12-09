def binary_search(arr,target):
    arr.sort()
    print(arr)
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (arr[left]+arr[right])//2
        if arr[mid]==target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else :
            right = mid - 1
    


arr = [2,3,1,6,9,0,4,9]
target = int(input("Enter Element to search: \n"))
print('Your item is on this index in array : ', binary_search(arr,target))