n = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

# 초기화
max_value = -10**9
min_value = 10**9


def dfs(depth, total, plus, minus, multiply, divide):
    global max_value, min_value
    if depth == n:
        if max_value < total :
            max_value = total
        if min_value > total :
            min_value = total
        return 
    if plus:
        dfs(depth+1, total + nums[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total - nums[depth], plus, minus-1, multiply, divide)        
    if multiply:
        dfs(depth+1, total * nums[depth], plus, minus, multiply-1, divide)        
    if divide:
        if total > 0 :
            dfs(depth+1, total // nums[depth], plus, minus, multiply, divide-1)        
        else:   
            dfs(depth+1, -(-total // nums[depth]), plus, minus, multiply, divide-1)        
            
dfs(1, nums[0], *operators)

print(max_value)
print(min_value)
