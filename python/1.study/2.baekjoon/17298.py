input()
nums = list(map(int, input().split()))
stack = []
nge = [-1 for _ in range(len(nums))]

for idx, num in enumerate(nums):
    while len(stack) > 0 and num > stack[-1][1]:
        nge[stack.pop()[0]] = num
    stack.append([idx, num])

for i in nge:
    print(i, end =' ')

