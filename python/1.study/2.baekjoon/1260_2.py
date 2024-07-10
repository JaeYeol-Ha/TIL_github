from collections import deque as dq

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1) ]

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

graph_list = dict()

for i in range(1, n+1):
    graph_list[i] = set(graph[i])

# print(graph_list)

def DFS_with_adj_list(graph, root, visited = []):
    for i in graph[root]:
        if i not in visited:
            visited.append(i)
            DFS_with_adj_list(graph, i, visited)
    return visited

print(DFS_with_adj_list(graph_list, v, [v]))

def BFS_with_adj_list(graph, root):
    visited = []
    q = dq([root])
    while q:
        n = q.popleft()
        if n not in visited:
            visited.append(n)
            q += graph[n] - set(visited)
    return visited

print(BFS_with_adj_list(graph_list, v))