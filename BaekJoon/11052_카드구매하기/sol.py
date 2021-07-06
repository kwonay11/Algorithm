N = int(input())
dp = [0]+list(map(int,input().split()))
#합이 N인것의 조합, dp[i]에 최댓값 갱신
for i in range(N+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i],dp[i-j]+dp[j])
print(dp[N])
