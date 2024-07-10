from itertools import combinations

heights = [int(input()) for _ in range(9)]

# 1번째 방법: combinations를 이용
def printSmallMan(combi):
    for heights in sorted(combi):
        print(heights, end=' ')

for combi in combinations(heights,7):
    if sum(combi) == 100:
        printSmallMan(combi)
        break

print()
# 2번째 방법: 그냥 알고리즘으로

def printSmallMan2(heights, i, j):
    for man in range(len(heights)):
        if man != i and man != j:
            print(heights[man], end=' ')

heights.sort()
tot = sum(heights)
for i in range(8):
    for j in range(i+1, 9):
        if tot - heights[i] -heights[j] == 100:
            printSmallMan2(heights, i, j)
            break