# for bfs

import sys
from collections import deque

input = sys.stdin.readline
t = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(y, x):
    q = deque()
    q.append([y, x])
    while q:
        y, x = q.popleft()
        if chk[y][x] :
            print(f"이미 체크 y,x:{y},{x}")
        # chk[y][x] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=ny<n and 0<=nx<m and arr[ny][nx] == 1 and not chk[ny][nx]:
                chk[ny][nx] = True
                q.append([ny, nx])

for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    chk = [[0] * m for _ in range(n)]
    마리수 = 0
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    for y in range(n):
        for x in range(m):
            if arr[y][x] == 1 and not chk[y][x]:
                마리수 += 1
                chk[y][x] = True
                bfs(y, x)
    print(마리수)