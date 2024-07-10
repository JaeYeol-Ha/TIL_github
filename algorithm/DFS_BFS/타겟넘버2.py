# def dfs(numbers, start=0):
#     visited = set()
#     stack = [(start, 0)] # sum
#     while stack :
#         node = stack.pop()
#         if node not in visited:
#             visited.add(node)
#             sum = node

from collections import deque
def solution(numbers,target):

    def bfs(numbers):
        # queue 셋팅
        queue = deque([(0, 0)])
        # 찾고싶은 값
        count = 0
        while queue:
            node, current_sum = queue.popleft()
            # 마지막 탐색인지
            if node == len(numbers): 
                # 찾을 값과 일치하는지
                if current_sum==target:
                    count +=1
            # 아니면 다음 탐색으로 이동
            else:
                queue.append((node+1, current_sum+numbers[node]))
                queue.append((node+1, current_sum-numbers[node]))
        return count

    def dfs(numbers):
        # queue 셋팅
        stack = [(0,0)]
        # 찾고싶은 값
        count = 0
        while stack:
            node, current_sum = stack.pop()
            # 찾을 값과 일치하는지
            if node == len(numbers):
                if current_sum==target:
                    count +=1
            # 다음 탐색으로 이동
            else:
                stack.append((node+1, current_sum+numbers[node]))
                stack.append((node+1, current_sum-numbers[node]))
        return count

    return dfs(numbers)
                


numbers =[1, 1, 1, 1, 1]	
target = 3
# dfs(numbers, 0)
print(solution(numbers, target))