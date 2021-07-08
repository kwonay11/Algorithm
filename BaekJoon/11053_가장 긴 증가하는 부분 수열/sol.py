N = int(input())
nums = list(map(int,input().split()))
# res = []
# for i in range(N):
#     cnt = 0
#     for j in range(i,N):
#         if nums[i] < nums[j]:
#             cnt += 1
#
#     res.append(cnt)
# print(res)
# print(max(res))

dp = [1]*N
for i in range(N):
    for j in range(i): #이전까지 작았다면 해당 dp것에 +1해서 max값 넣기
        if nums[i] > nums[j]:
            dp[i] = max(dp[i],dp[j]+1) #메모이제이션
print(max(dp))
print(dp)