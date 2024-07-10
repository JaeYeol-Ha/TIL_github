# 1 3 / 23,,1
# 1 2 / 3,2,1
# 3 2 / 3,12,
# 1 3 / ,12,3
# 2 1 / 1,2,3
# 2 3 / 1,,23
# 1 3 / ,,123
from collections import deque
a, b, c = deque(), deque(), deque()
n = int(input())  # 원판 개수
for i in range(1, n+1):
    a.append(i)
print(a)


