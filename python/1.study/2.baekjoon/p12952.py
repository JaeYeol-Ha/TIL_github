def dfs(depth):
    global count
    if depth == n:
        count += 1
        print(f'--graph--{graph}')
        return

    for i in range(n):
        if visited[i] == 0:  # 해당 자리에 퀸이 존재하는지 확인 (세로줄)
            graph[depth] = i  # 각 행마다 위치하는 퀸의 자리 (0번째 열에 i 배치)
            promising = True # 가능할지
            for j in range(depth):   # graph의 개수만큼 for문을 돌려야하지만 어차피 depth랑 개수 똑같음
                if abs(graph[depth]-graph[j]) == abs(depth-j): # |y2-y1| == |x2-x1|
                    promising = False
                    break           
            if promising:
                print(graph, depth)
                visited[i] = 1
                dfs(depth+1)
                visited[i] = 0
    
n = int(input())

graph = [0]*n
visited = [0]*n

count = 0
dfs(0)
print(count)