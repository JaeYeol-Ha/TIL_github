from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):

    # 캐릭터움직임
    dy = (0, 0.5, 0, -0.5)
    dx = (0.5, 0, -0.5, 0)

    # 지형(map) 최대값 찾기
    MAX_Y = 0
    MAX_X = 0
    for rec in rectangle:
        MAX_Y = max(MAX_Y, rec[3])
        MAX_X = max(MAX_X, rec[2])

    # 올바른 좌표 찾기
    def is_valid_coord(y, x):
        # print(f"is_valid_coord: x,y,MAX_X,MAX_Y : {x, y, MAX_X, MAX_Y}")
        if 0 <= y <= MAX_Y and 0 <= x <= MAX_X:
            return True
        return False

    def is_on_the_load(y, x, ny, nx):
        # print(f"x,y,nx,ny:{x,y,nx,ny}")
        for rec in rectangle:
            x1, y1, x2, y2 = rec
            if (y1 <= y <= y2) and (y1 <= ny <= y2) and ((x1 == x and x1 == nx) or (x2 == x and x2 == nx)):
                # print(f"세로이동: {y1} <= {y},{ny} <= {y2} and (({x1} == {x},{nx}) or ({x2} == {x},{nx}))")
                return True
            if ((y1 == y and y1 == ny) or (y2 == y and y2 == ny)) and (x1 <= x <= x2) and (x1 <= nx <= x2):
                # print(f"가로이동: (({y1} == {y},{ny}) or ({y2} == {y},{ny})) and ({x1} <= {x},{nx} <= {x2})")
                return True
        return False

    # 두 사각형의 충돌 지점인가
    def is_crash_point(y, x):
        for rec in rectangle:
            x1, y1, x2, y2 = rec
            if x1 < x < x2 and y1 < y < y2:
                # print(f"is_crash_point: {x1} < {x} < {x2} and {y1} < {y} < {y2}")
                return True
        return False

    def bfs():
        q = deque([(characterY, characterX, 0)])
        chk = [(characterY, characterX)]  # x, y를 지나갔는지 체크
        # chk.append((2, 1))
        while q:
            y, x, d = q.popleft()
            if (y, x) == (itemY, itemX):
                return int(d)
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if is_valid_coord(ny, nx) and (ny, nx) not in chk and is_on_the_load(y, x, ny, nx) and not is_crash_point(ny, nx):
                    # print(f"{y,x}에서 {ny,nx}로 가는중, 거리:{d+0.5}")
                    chk.append((ny, nx))
                    q.append((ny, nx, d+0.5))

    return bfs()

# rectangle	= [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
# characterX	= 1
# characterY	= 3
# itemX	= 7
# itemY	= 8


rectangle,characterX,characterY,itemX,itemY	=		[[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1
print(solution(rectangle, characterX, characterY, itemX, itemY))

