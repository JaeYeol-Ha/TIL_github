# for bfs

import sys
from collections import deque as dq
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

cnt = 0
maxsize = 0

def bfs(y, x):
    q = dq()
    q.append([y, x])
    size = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m and arr[ny][nx] == 1 and not chk[ny][nx]:
                chk[ny][nx] = True
                q.append([ny,nx])
                size += 1    
    return size

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not chk[i][j]:
            chk[i][j] = True
            cnt += 1
            maxsize = max(maxsize, bfs(i, j))
print(cnt)
print(maxsize)