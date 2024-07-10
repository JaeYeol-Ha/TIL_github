import sys
n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(list(sys.stdin.readline().split()))

nums.sort(key = lambda x:int(x[0]))

for i in nums:
    print(i[0],i[1])