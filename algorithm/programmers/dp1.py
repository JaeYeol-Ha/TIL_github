# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        newScoville = heapq.heappop(scoville)+(heapq.heappop(scoville)*2)
        heapq.heappush(scoville, newScoville)
        answer += 1
        if len(scoville)==1 and scoville[0]<K:
            return -1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))