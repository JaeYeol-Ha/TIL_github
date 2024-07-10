# DFS(백트래킹) 사용
def dfs():
    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    for i in range(1, n+1):
        s.append(i)
        dfs()
        s.pop()

n, m = map(int, input().split())
s = []

dfs()