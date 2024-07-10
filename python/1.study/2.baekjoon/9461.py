dp = [0] * 101

dp[1] = 1
dp[2] = 1
dp[3] = 1 
dp[4] = 2 
dp[5] = 2 
dp[6] = 3 # dp[5] + dp[1]
dp[7] = 4 # dp[6] + dp[2]
dp[8] = 5 # dp[7] + dp[3]
dp[9] = 7 # dp[8] + dp[4]
dp[10] = 9 # dp[9] + dp[5]

for i in range(6,101):
    dp[i] = dp[i-1] + dp[i-5]

t = int(input())
while t > 0:
    print(dp[int(input())])
    t-=1
