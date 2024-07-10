from collections import deque

# dfs에 필요한 요소: 현재티켓ticket, 다음티켓next_ticket, 최종목표finish_num, 최종경로navigate

# dfs: 현재티켓, 지난거리, 지나온경로, 최종거리, 체크포인트
def solution(tickets):

    def dfs(ticket, route, final_length, chk):
        if tickets


    chk = []
    tickets.sort()
    for ticket in tickets:
        if ticket[0] == "ICN":
            dfs(ticket, 2, ticket, len(tickets)+1, chk)            
    return 


tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))
