import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

prefix_sum = [nums[0]]

for i in nums:
    prefix_sum.append(i + prefix_sum[-1])

for i in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])

