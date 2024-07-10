# Counter 시간복잡도 : O(n)
# print(Counter(elem).most_common()[0][1])

n, x = 7, 2
elem = [1, 1, 2, 2, 2, 2, 3]
n = len(elem)


def binary_search(elem, x, n, start=0, end=n-1):
    while start <= end:
        mid = (start+end)//2
        if elem[mid] == x:
            return mid
        elif elem[mid] < x:
            start = mid + 1
        elif elem[mid] > x:
            end = mid - 1
    return -1

# 값이 존재하는지 찾기
mid = binary_search(elem, x, n)

if mid == -1: # 값이 없으면
    print(-1)
else: # 값이 있으면 범위 찾기(이진탐색)
    min_x, max_x = mid, mid
    min_x_result, max_x_result = -1, -1

    while min_x > 0:
        min_x_result = min_x
        min_x = binary_search(elem, x, n, 0, min_x-1)
    while max_x > 0:
        max_x_result = max_x
        max_x = binary_search(elem, x, n, max_x+1, n)

    print(max_x_result - min_x_result + 1)
