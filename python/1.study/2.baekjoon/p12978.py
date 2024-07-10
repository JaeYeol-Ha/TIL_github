import heapq


def to_grapify(roads, N):
    graph = [[] for _ in range(N+1)]
    for road in roads:
        a, b, c = road
        graph[a].append((b, c))
        graph[b].append((a, c))
    return graph


def solution(N, road, K):
    count = 0
    q = []
    INF = int(1e9)
    distance = [INF] * (N+1)
    graph = to_grapify(road, N)
    heapq.heappush(q, (0, 1))
    distance[1] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))
    for dist in distance[1:]:
        if dist <= K :
            count+=1
    return count  # 음식배달가능한마을수


N = 5  # 마을수
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
# [시작,도착,시간]
K = 3  # 배달가능시간

print(solution(N, road, K))
