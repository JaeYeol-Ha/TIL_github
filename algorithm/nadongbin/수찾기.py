# 1920

# n = int(input())
# arr = list(map(int, input().split()))
# m = int(input())
# chks = list(map(int, input().split()))

n = 5
arr = [4, 7, 5, 2, 3]
m = 5
chks = [1, 3, 7, 9, 5]

arr.sort()
def binary_search(arr, chk):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == chk:
            print(1)
            return
        elif arr[mid] < chk:
            start = mid + 1
        else:
            end = mid - 1
    print(0)

for chk in chks:
    binary_search(arr,chk)
