# 명함지갑
def solution(sizes):
    answer = 0
    width=0
    height=0
    # 1. 각 명함의 사이즈를 확인하자.
    for size in sizes:
        # 2. 세로가 더 긴 놈들은 다 가로로 눞히자.
        if size[0] < size[1]: 
            size = size[::-1]
        width = max(width, size[0])
        height = max(height, size[1])
    answer = width*height    
    return answer

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))

## 최적화
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)