from collections import defaultdict
from collections import deque as dq
from pprint import pprint as print

n, m = map(int, input().split())
start = [0, 0]

matrix = []
for i in range(n):
    row = list(map(int, input()))
    matrix.append(row)

# print(matrix)

x = [1, -1, 0, 0]
y = [0, 0, -1, 1]


def bfs(matrix):
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    print(visited)
