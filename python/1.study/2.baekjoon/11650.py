import sys
n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(list(map(int,sys.stdin.readline().split())))

nums.sort()

for i in nums:
    print(i[0],i[1])