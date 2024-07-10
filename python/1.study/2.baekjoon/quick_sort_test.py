from cmath import e
from operator import eq


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lesser_arr, equal_arr, greater_arr = [],[],[]
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else :
            equal_arr.append(num)            
    return quicksort(lesser_arr) + equal_arr + quicksort(greater_arr)


arr = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print(quicksort(arr))
