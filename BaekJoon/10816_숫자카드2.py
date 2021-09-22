N = int(input())
card = list(map(int,input().split()))
have = {}
for i in range(N):
    if card[i] not in have:
        have[card[i]] = 1
    else:
        have[card[i]] += 1

M = int(input())
card2 = list(map(int,input().split()))
for i in range(M):
    if card2[i] in have:
        print(have[card2[i]],end=' ')
    else:
        print(0,end=' ')

