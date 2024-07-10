from collections import deque

numbers = [1,1,1,1,1]
target = 3


def bfs(numbers, target):
    ans = 0
    q = deque()
    max_len = len(numbers)
    q.append((numbers[0], 1))
    q.append((-numbers[0], 1))
    while q:
        num, l = q.popleft()
        if l < max_len:
            q.append((numbers[l]+num, l+1))
            q.append((-numbers[l]+num, l+1))
        elif num == target:
            ans += 1
    return ans



def solution(numbers, target):
    print(bfs(numbers, target))


solution(numbers, target)