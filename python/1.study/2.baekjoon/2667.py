n = int(input())
maps = []
for i in range(n):
    maps.append(list(map(int, input())))
visited = [[False]*n for _ in range(n)]
# print(maps)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
group_count = 0
house_count = 0
house_count_by_group = []

def dfs(i, j):
    if maps[i][j] > 0 and not visited[i][j]:
        maps[i][j] = group_count
        visited[i][j] = True
        global house_count
        house_count += 1
        for d in range(4):
            if n > i+dx[d] >= 0 and n > j+dy[d] >=0:
                dfs(i+dx[d], j+dy[d])
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            group_count += 1
            house_count_by_group.append(house_count)
            house_count = 0

print(group_count)
house_count_by_group.sort()
for i in house_count_by_group:
    print(i)
# for m in maps:
#     print(m)
