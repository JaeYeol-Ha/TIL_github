from collections import deque

n, m = 4, 5
arr = [[0, 0, 1, 1, 0],
       [0, 0, 0, 1, 1],
       [1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0]]

count = 0  # 아이스크림 만들어지는 개수

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(y, x):
    arr[y][x] = 1
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] == 0:
            dfs(ny, nx)

def bfs(y,x):
    

for y in range(n):
    for x in range(m):
        if arr[y][x] == 0:
            count += 1
            dfs(y, x)

print(count)
