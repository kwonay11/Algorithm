########시간초과#####
N = int(input())
line = list(map(int, input().split()))
cnt = []

for i in range(N):
    for j in range(1,N):
        if i < j:
            if j not in cnt and line[i] > line[j]:
                cnt.append(j)

print(len(cnt))