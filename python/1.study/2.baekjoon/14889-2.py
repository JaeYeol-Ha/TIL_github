n = int(input())
graph = [ list(map(int,input().split())) for _ in range(n)]
min_diff = int(1e9)
s = []

def dfs(start):
    if len(s) == n//2:
        global min_diff
        stat1, stat2 = 0, 0
        for i in range(n):
            for j in range(n):
                if i in s and j in s:
                    stat1 += graph[i][j]
                elif i not in s and j not in s:
                    stat2 += graph[i][j]
        min_diff = min(min_diff, abs(stat1-stat2))
        return
    for i in range(start, n):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()

dfs(0)
print(min_diff)