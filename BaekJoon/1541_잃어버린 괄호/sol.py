# 50-50+40-30+70-20
nums = input().split('-')
print(nums)
res = 0
#맨 첫꺼는 더하기
for i in nums[0].split('+'):
    res += int(i)

for i in range(1,len(nums)):
    temp = nums[i].split('+')
    temp_sum = 0
    for j in range(len(temp)):
        temp_sum += int(temp[j])
    res -= temp_sum
print(res)

