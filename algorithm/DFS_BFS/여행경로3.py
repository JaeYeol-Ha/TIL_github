## deque에 필요한 요소 : 현재 정점, 지나온 거리, 현재까지 경로, 지났던 정점 체크포인트

def solution(tickets):
    # 알파벳 순으로 정렬
    tickets.sort()
    candidates = []
    finish_count = len(tickets) # 티켓 수 만큼 최단거리 탐색
    
    def dfs(ticket, count, order, chk):
        for idx, ticket in enumerate(tickets):
            # 이미 간 티켓 제외 and 다음 출발지 == 이전 도착지
            if idx not in chk and ticket[0] == order[-1]:
                # 마지막 티켓이라면 후보에 넣고
                if count == finish_count:
                    candidates.append(order+[ticket[1]])
                # 아니면 deque에 넣고
                else:
                    dfs(ticket, count+1, order+[ticket[1]], chk+[idx])

    for idx, ticket in enumerate(tickets):
        if ticket[0] == "ICN":
            dfs(ticket, 2, ticket, [idx])

    return sorted(candidates)[0]


tickets = [["ICN", "JFK"], ["JFK", "ICN"], ["ICN", "JFK"]]
print(solution(tickets))
