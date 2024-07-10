# N-Queen

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def print_maps(maps):
    for map in maps:
        print(map)


def init_map(n):
    maps = [[0]*n for _ in range(n)]
    chk = [[False]*n for _ in range(n)]
    # print_maps(maps)
    return maps, chk


def dfs(y, x, maps, chk, n):
    for nx in range(n):
        if 0 <= y < n and 0 <= nx < n and not chk[y][nx]:
            chk[y][nx] = True
    for ny in range(n):
        if 0 <= ny < n and 0 <= x < n and not chk[ny][x]:
            chk[ny][x] = True
    for i in range(-n, n):
        if 0 <= y+i < n and 0 <= x+i < n and not chk[y+i][x+i]:
            chk[y+i][x+i] = True
        if 0 <= y+i < n and 0 <= x-i < n and not chk[y+i][x-i]:
            chk[y+i][x-i] = True            


def solution(n):
    maps, chk = init_map(n)
    count = 0
    for y in range(n):
        for x in range(n):
            if not chk[y][x]:
                chk[y][x] = True
                maps[y][x] = 1
                count += 1
                dfs(y, x, maps, chk, n)
    print_maps(maps)
    return 0


n = 4
print(solution(4))
