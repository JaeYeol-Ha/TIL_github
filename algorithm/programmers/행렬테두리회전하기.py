def print_matrix(matrix):
    for row in matrix:
        print(row)


def draw_matrix(rows, columns):
    return [[col+(row*columns) for col in range(1, columns+1)] for row in range(rows)]


def rotate_matrix(matrix, query):
    y1, x1, y2, x2 = query
    x, y = x1, y1
    tmp = matrix[y][x]
    min_val = tmp
    # [y][x] = (2,2) , (2,3), (2,4), (4,3), (4,4), (5,4) ...
    # 오른쪽으로 이동
    while x < x2:
        tmp, matrix[y][x+1] = matrix[y][x+1], tmp
        min_val = min(min_val, tmp)
        x += 1
    # 아래로 이동
    while y < y2:
        tmp, matrix[y+1][x] = matrix[y+1][x], tmp
        min_val = min(min_val, tmp)
        y += 1
    # 왼쪽 이동
    while x > x1:
        tmp, matrix[y][x-1] = matrix[y][x-1], tmp
        min_val = min(min_val, tmp)
        x -= 1
    # 위로 이동
    while y > y1:
        tmp, matrix[y-1][x] = matrix[y-1][x], tmp
        min_val = min(min_val, tmp)
        y -= 1
    return min_val


def solution(rows, columns, queries):
    result = []
    matrix = draw_matrix(rows, columns)
    # N번의 회전 수행
    for query in queries:
        # x1, y1, x2, y2의 순번이 1번부터 시작해서 0번으로 수정하여 반영
        for i in range(4):
            query[i] = query[i] - 1
        min_val = rotate_matrix(matrix, query)
        result.append(min_val)
    # print_matrix(matrix)
    return result


rows, columns = 6, 6
queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]

print(solution(rows, columns, queries))
