## itertools를 이용하는 방법
# from itertools import combinations_with_replacement
# n, m = map(int, input().split())

# result = ""
# for arr in sorted(list(combinations_with_replacement([i for i in range(1, n+1)], m))):
#     for i in arr:
#         result += str(i) + ' '
#     result += '\n'
# print(result)

# DFS(백트래킹) 사용
# 순열
def dfs():
    if len(s) == m:
        print(' '.join(map(str,s)))
    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

n, m = map(int, input().split())
s = []

dfs()