N = int(input())
P = list(map(int, input().split()))
NP = sorted(P)
sum_NP = []
tmp = 0
for i in range(len(NP)):
    tmp += NP[i]
    sum_NP.append(tmp)


print(sum(sum_NP))
