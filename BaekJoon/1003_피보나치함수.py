T=int(input())
dp = [[1,0] for _ in range (40)]
dp[1] = [0,1]

for i in range(2,40):
    dp[i] = [dp[i-1][0] + dp[i-2][0],dp[i-1][1] + dp[i-2][1]]

for i in range(T):
    num = int(input())
    print(dp[num][0],dp[num][1])


