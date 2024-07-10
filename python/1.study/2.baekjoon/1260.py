from collections import deque as dq

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1) ]
visit1 = [False] * (n+1)
visit2 = [False] * (n+1)
output1 = ""
output2 = ""

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in range(n+1):
    graph[i].sort()

def dfs(v):
    global output1
    visit1[v] = True
    output1 += str(v) + ' '
    for i in graph[v]:
        if not visit1[i]:
            dfs(i)

def bfs(v):
    global output2
    q = dq()
    q.append(v)
    while q :
        v = q.popleft()
        if not visit2[v]:
            output2 += str(v) + ' '
            visit2[v] = True
            for i in graph[v]:
                q.append(i)

dfs(v)
print(output1)
bfs(v)
print(output2)