N = int(input())
nums = list(map(int,input().split()))
array = []
for i in range(N):
    array.append([nums[i],i])
# print(array)
array = sorted(array, key=lambda x: x[0])
# print(array)
li = [0] * N
li[array[0][1]] = 0
cnt = 1
for i in range(1,N):
    if array[i][0] == array[i-1][0]:
        li[array[i][1]] = li[array[i-1][1]]
        continue
    li[array[i][1]] = cnt
    cnt += 1
for i in range(N):
    print(li[i],end=" ")
