from itertools import combinations

N,M = map(int,input().split())
cards = list(map(int,input().split()))

combi = list(combinations(cards,3)) #3개 조합 뽑기
# print(combi)
high = 0
for i in range(len(combi)):
    num = sum(combi[i]) #각 조합의 합
    if high < num and num <= M: #합이 M보다 크지 않을 때 최대값 갱신
        high = num
print(high)