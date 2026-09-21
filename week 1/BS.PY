def binarysearch(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


arr = [1, 4, 5, 7, 78, 95]
target = 95

print(binarysearch(arr, target))