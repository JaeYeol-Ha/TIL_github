graph = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0],
]


# 인접행렬에서 DFS 찾기
def dfs(graph, start=0, visit=None, result=None):
    if visit is None:
        visit = [False] * len(graph)
    if result is None:
        result = []

    visit[start] = True
    result.append(start)

    for neighbor, connected in enumerate(graph[start]):
        if connected and not visit[neighbor]:
            dfs(graph, neighbor, visit, result)
    return result


dfs(graph)
# 123123
