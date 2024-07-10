def solution(bricks, n, k):
    select = selectBricks(bricks[1:-1], k-1)
    min_bricks = n*k-1
    for arr in select:
        temp = n*(k-1) - sum(arr)
        if min_bricks > temp:
            min_bricks = temp
    return min_bricks

def selectBricks(bricks, toPick): 
    result = []
    if toPick == 0: return [[]]
    for i in range(len(bricks)):
        pick = bricks[i]        
        for rest in selectBricks(bricks[i+2:], toPick-1):
            result.append([pick]+rest)
    return result

print(solution(bricks = [1,2,5,3,1,0,2,3], n = 6, k = 3))

# bricks의 길이는 5 이상 20 이하입니다.
# bricks의 원소는 0 이상 49 이하인 정수입니다.
# n은 1 이상 50 이하인 자연수입니다.
# [물의 높이] n은 bricks의 원소 중 가장 큰 값 보다 항상 큽니다.
# 즉, 처음에 지형을 위쪽에서 바라봤을 때 보이는 물 웅덩이는 항상 1개입니다.
# [웅덩이개수] k는 2 이상 (bricks의 길이 + 1) / 2 이하인 자연수입니다.
