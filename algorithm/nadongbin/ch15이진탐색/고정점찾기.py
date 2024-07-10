n = 5
a = [-15, -4, 0, 1, 13]


def fixed_point(a, start=0, end=n-1):
    while start <= end:
        mid = (start+end)//2
        if a[mid] == mid:
            return mid
        elif a[mid] < mid:
            start = mid+1
        elif a[mid] > mid:
            end = mid-1
    return -1

print(fixed_point(a))