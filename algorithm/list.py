arr = []

arr.append(0)
arr.sort()
arr.reverse()

idx, num = 0, 3
arr.insert(idx, num)
arr.remove(num)
print(arr)

# 여러개 remove 예시
a = [i for i in range(5)]
remove_set = {3,5}
result = [i for i in a if i not in remove_set]
print(result)