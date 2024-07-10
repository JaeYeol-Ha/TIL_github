import sys
sys.setrecursionlimit(2000) #최대 재귀를 늘려줘야 런타임 에러를 피할 수 있다

t = int(input())

def dfs(i):
    if check[i] == 0:
        check[i] = 1
        dfs(arr[i])
        return 1
    return 0

for _ in range(t):
    n = int(input())
    arr = [1] + list(map(int,input().split()))
    check = [0] * (n+1)
    count = 0
    for i in range(1, n+1):
        count += dfs(i)
    print(count)