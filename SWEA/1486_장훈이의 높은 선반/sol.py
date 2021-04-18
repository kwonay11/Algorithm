import sys
sys.stdin = open("input.txt")

from itertools import combinations

T = int(input())
#높이가 B 이상인 탑 중에서 높이가 가장 낮은 탑
#조합을 구하여 합이 B보다 큰것의 리스트를 만든다.
for tc in range(1,T+1):
    N, B = map(int,input().split()) # N:점원 수 B:선반의 높이
    H = list(map(int,input().split()))
    over = []
    sum_o = []
    for i in range(N+1):
        over.append(list(combinations(H,i)))
        for j in range(len(over[i])):
            if sum(over[i][j]) >= B:
                sum_o.append(sum(over[i][j]))

    print("#{} {}".format(tc, min(sum_o)-B))