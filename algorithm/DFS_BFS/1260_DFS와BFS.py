from collections import defaultdict
from collections import deque as dq

n, m, v = map(int, input().split())

# 인접 행렬 만들기
matrix = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

# 행렬 오름차순 정렬
for key in matrix.keys():
    matrix[key].sort()


def dfs(matrix, start=v):
    visited = [False] * (n + 1)
    stack = dq([start])
    visit = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            visit.append(node)
            visited[node] = True
            for adjacent in list(reversed(matrix[node])):
                if not visited[adjacent]:
                    stack.append(adjacent)
    return visit


def bfs(matrix, start=v):
    visited = [False] * (n + 1)
    queue = dq([start])
    visit = []
    while queue:
        node = queue.popleft()
        if not visited[node]:
            visit.append(node)
            visited[node] = True
            for adjacent in matrix[node]:
                if not visited[adjacent]:
                    queue.append(adjacent)
    return visit


def print2(list):
    for i in list:
        print(i, end=" ")


print2(dfs(matrix, v))
print()
print2(bfs(matrix, v))
