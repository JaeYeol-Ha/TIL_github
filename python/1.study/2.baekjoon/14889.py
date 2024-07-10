n = int(input())
graph = [ list(map(int,input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
min_diff = int(1e9)

def dfs(depth=0, idx=0):
    global min_diff          # 최적해는 global로 뺀다.
    if depth == n//2:        # dfs 종료 조건
        stat1, stat2 = 0, 0
        for i in range(n):          # i, j 둘다 방문으로 체크된경우에 능력치 합산
            for j in range(n):
                if visited[i] and visited[j]:
                    stat1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    stat2 += graph[i][j]
        min_diff = min(min_diff, abs(stat1-stat2))
    for i in range(idx, n):
        visited[i] = True
        dfs(depth+1, i+1) 
        visited[i] = False

dfs()

print(min_diff)