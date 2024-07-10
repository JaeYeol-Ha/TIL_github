import sys
n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

sorted_nums = list(set(nums))
sorted_nums.sort()

dict_nums = dict()
for idx,num in enumerate(sorted_nums):
    dict_nums[num] = idx

ziped_nums = []
for i in nums:
    print(dict_nums.get(i), end=' ')

    
