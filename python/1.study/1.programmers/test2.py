import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
chk = [[False]*m for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

count = 0 
maxsize = 0
def bfs(y,x):
    q = deque()
    q.append([y,x])
    size = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and maps[ny][nx] == 1 and not chk[ny][nx]:
                chk[ny][nx] = True
                size +=1
                q.append([ny,nx])
    return size
    

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 and not chk[i][j]:
            chk[i][j] = True
            count +=1
            maxsize = max(maxsize, bfs(i,j))

print(count)
print(maxsize)
