from itertools import combinations

N, K = map(int, input().split())
num = list(map(int, input().split()))

cn = list(combinations(num, 3))

cnt = 0

print(cn)
for i in range(len(cn)):
    ans = 1
    for n in cn[i]:
        ans *= n

    if ans % K == 0:
        cnt += 1

print(cnt)


