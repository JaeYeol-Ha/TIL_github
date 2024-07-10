n = int(input())
p = list(map(int, input().split()))
# 0. init
print(p)

# 1. when not sort
k = []
sum = 0
sumsum = 0
for i in p:
    sum += i
    sumsum += sum
    k.append(sumsum)
print(k)

# 2. when sort
k = []
sum = 0
sumsum = 0
p.sort()
for i in p:
    sum += i
    sumsum += sum
    k.append(sumsum)
print(k[-1])

