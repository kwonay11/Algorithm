N, M = map(int, input().split())
lst =list(map(int, input().split()))

cnt = 0

for i in range(N):
    num_sum = lst[i]
    if num_sum == M:
        cnt += 1
        continue
    for j in range(i+1, N):
        num_sum += lst[j]
        if num_sum == M:
            cnt += 1
            break
        elif num_sum > M:
            break
print(cnt)