N = int(input())
dp = [0]*(N+1)

for i in range(1,N+1):
    if (i**0.5)%1 == 0.0:
        dp[i] = 1
    else:
        a = int(i**0.5)**2
        if i % a == 0: #배수
            dp[i] = dp[a]*(i//a)

        else:
            dp[i] = dp[a]+(i-a)

print(dp[N])
# print(dp)