n = int(input())
nums = list(map(int,input().split()))
# # 리스트에 왼쪽부터 더한 누적값이 자기 자신보다 크다면 그 리스트에 넣어줌 작다면 자기 자신값 넣어줌
for i in range(1,n):
    nums[i] = max(nums[i],nums[i-1]+nums[i])
print(max(nums))

