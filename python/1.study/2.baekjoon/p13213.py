# 프로그래머스 Ch14-2. BFS,DFS_가장 먼 노드 실습

from collections import deque


def bfs(n, arr):
    dist_arr = [0 for _ in range(n+1)]  # a번째 거리에 b개의 노드가 있다. : [1,2,3,...,b]
    chk = [True, True] + [False for _ in range(n+1)]
    q = deque([(1, 0)])
    while q:
        node, length = q.popleft()
        for next_node in arr[node]:
            if not chk[next_node]:
                chk[next_node] = True
                dist_arr[length] += 1
                q.append((next_node, length+1))
    for i in dist_arr[::-1]:
        if i > 0:
            return i
    return 1


def solution(n, vertex):
    arr = [[] for _ in range(n+1)]
    for a, b in vertex:
        arr[a].append(b)
        arr[b].append(a)
    return bfs(n, arr)


n, vertex = 7,	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2], [6, 7]]
# arr = [[], [3, 2], [3, 1, 4], [6, 4, 2, 1], [3, 2], [2], [3]]
print(solution(n, vertex))
