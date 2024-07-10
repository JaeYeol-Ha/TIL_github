import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

max_count = 0

def dfs(y, x, chk, high):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < n and 0 <= nx < n and maps[ny][nx] > high and not chk[ny][nx]:
            chk[ny][nx] = True
            dfs(ny, nx, chk, high)


for high in range(101):
    chk = [[False]*n for _ in range(n)]
    count = 0
    for y in range(n):
        for x in range(n):
            if maps[y][x] > high and not chk[y][x]:
                chk[y][x] = True
                count += 1
                dfs(y, x, chk, high)
    # print(f'high:{high}, count:{count}')
    if count == 0:
        break                
    max_count = max(max_count, count)
    

print(max_count)