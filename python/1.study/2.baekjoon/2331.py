# d[0] = a
# d[n] = d[n-1][0]^p + d[n-1][1]^p + ...
import math

a, p = map(int,input().split())
d = [a]

while True:
    last_num = str(d[-1])
    next_num = 0
    for n in last_num:
        next_num += int(math.pow(int(n),p))
    if next_num in d:
        break
    d.append(next_num)

print(d.index(next_num))
