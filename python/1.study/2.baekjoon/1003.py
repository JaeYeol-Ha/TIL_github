dp = [[0,0] for _ in range(41)]
dp[0] = [1,0]
dp[1] = [0,1]
def fibonacci(n):
    if dp[n] != [0,0]:
        return dp[n]
    else:
        dp[n] = [fibonacci(n-1)[0] + fibonacci(n-2)[0], fibonacci(n-1)[1] + fibonacci(n-2)[1]] 
        return dp[n]

T = int(input())

for i in range(T):
    n = int(input())
    answer = fibonacci(n)
    print(answer[0], answer[1])
    