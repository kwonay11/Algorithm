N = int(input())
#점화식 dp[i] = dp[i-1]+dp[i-2]
dp = [0] * (N+1)
dp[1] = 1
if N > 1:
    dp[2] = 2

for i in range(3,N+1):
    dp[i] = (dp[i - 1] % 10007 + dp[i - 2] % 10007) % 10007
# print(dp)
print(dp[N])
