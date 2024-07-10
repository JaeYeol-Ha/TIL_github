computer = int(input())
n = int(input())
network = [[] for _ in range(computer+1)]
visited = [False for _ in range(computer+1)]
for i in range(1, n+1):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

count = 0
def dfs(v):
    visited[v] = True
    for i in network[v]:
        if not visited[i]:
            dfs(i)
            global count
            count += 1
    return count

print(dfs(1))
