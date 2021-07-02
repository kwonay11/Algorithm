```python
# 점화식 dp[i] = (dp[i-1] + 2*dp[i-2])

N = int(input())
dp = [0] * (N+1)
dp[1] = 1
if N > 1:
    dp[2] = 3
for i in range(3,N+1):
    dp[i] = (dp[i-1] + 2*dp[i-2])%10007
print(dp[N])
```

| N    | 블럭 |
| ---- | ---- |
| 1    | 1    |
| 2    | 3    |
| 3    | 5    |

이므로 

점화식 dp[i] = (dp[i-1] + 2*dp[i-2])