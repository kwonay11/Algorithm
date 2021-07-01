from itertools import combinations
N = int(input())
P = list(map(int,input().split()))
res = []
temp =[]
nums = []
temp2 =[]
for i in range(N):
    nums.append(i+1)
print(nums)

for i in range(N):
    temp = []
    temp = combinations(nums,i)
    if sum(list(temp)) == N: #temp의 합이 N과 같다면 해당값-1이 P의 인덱스이므로
        print(list(temp))
        temp2 =[]
        for j in temp:
            temp2.append(P[i-1])
        res.append(sum(temp2))
    print(res)

###아직 못품