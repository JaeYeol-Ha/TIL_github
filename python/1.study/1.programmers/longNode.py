import collections
n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

def solution(n, edge):
    dists = {i:0 for i in range(1, n+1)}
    edge = collections.defaultdict(list)

    for v,u in vertex:
        edge[v].append(u)
        edge[u].append(v)

    q = collections.deque(edge[1])
    dist = 1
    while q :
        for i in range(len(q)):
            v = q.popleft()
            if dists[v] == 0:
                dists[v] == dist

                for w in edge[v]:
                    q.append(w)
        dist +=1

    del dists[1]
    
    max_value = max(dists.values())
    answer = 0
    for v in dists.values():
        if v == max_value:
            answer += 1
            
    return 0



print(solution(n,vertex))