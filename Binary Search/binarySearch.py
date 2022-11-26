def binarySearch(array, target):
    '''
    Pre-condition: Array is sorted
    '''

    left = 0
    right = len(array) - 1

    while(left <= right):
        mid = (left + right) // 2
        if(array[mid] == target):
            return mid
        elif(array[mid] < target):
            left = mid + 1
        else:
            right = mid - 1

    return -1


array = [1, 2, 3, 4, 5]
target1 = 3
target2 = 6

print(binarySearch(array, target1))
print(binarySearch(array, target2))
