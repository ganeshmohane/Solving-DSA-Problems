# remove nth element from array - Zeus Learning (20 Sep 2024 APT test)

def remove_nth(arr, n):
    i = 0
    while i < len(arr):
        if arr[i] == n:
            arr.pop(i)
        else:
            i += 1

arr = [2, 3, 4, 5, 6]
print(arr)
n = int(input("Enter the number to delete it: \n"))
remove_nth(arr, n)
print(arr)

    