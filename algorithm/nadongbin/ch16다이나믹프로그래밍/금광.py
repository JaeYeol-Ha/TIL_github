# 풀이 방법 :
# matrix[0][0] => [0][1] => 이미 풀었으면(isSolved) 최대값(max)으로
#                 [1][1]
# matrix[1][0] => [0][1]
#                 [1][1]
#                 [2][1]
# matrix[2][0] => ...

rows, cols = 3, 4
arr = [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7]


def mining(rows, cols, matrix, stacked):
    # 1번 째 열부터 순서대로 진행, 라인별로 채굴
    for col in range(cols):
        for row in range(rows):
            if col == 0:
                stacked[row][col] = matrix[row][col]
            elif cols > col > 0:
                left_up = 0 if (row == 0) else stacked[row-1][col-1]
                left_down = 0 if row >= rows-1 else stacked[row+1][col-1]
                left = stacked[row][col-1]
                stacked[row][col] = max(
                    left_up, left, left_down) + matrix[row][col]


def solution(rows, cols, arr):
    matrix = [arr[i*cols:(i+1)*cols] for i in range(rows)]
    stacked = [[0 for _ in range(cols)] for _ in range(rows)]
    mining(rows, cols, matrix, stacked)
    return max(stacked[row][-1] for row in range(rows))


print(solution(rows, cols, arr))
