n, c = 5, 3
x = [1, 2, 8, 4, 9]

x.sort()


def binary_search(array, start, end):
    answer = 0
    while start <= end:
        mid = (start+end)//2
        current = array[0]
        count = 1
        for i in range(1, len(array)):
            if array[i] >= current + mid:
                count += 1
                current = array[i]
        if count >= c:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    return answer


print(binary_search(x, 1, x[-1] - x[0]))
