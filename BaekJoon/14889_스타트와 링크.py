from itertools import combinations
import sys

input = sys.stdin.readline
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]

members = [i for i in range(N)] #0부터 N까지 리스트 만들어놓고 조합 뽑음

# 첫 조합의 여집합 <>반대되는거는 마지막에 있는 조합
#i번째면 -i-1번째가 반대되는 것
combi = []
#두개씩 뽑고 그것들을 리스트에 넣은 다음에
for team in list(combinations(members, N//2)):
    combi.append(team)

A = []
B = []
for i in range(len(combi)//2):
    # print(combi[i])
    temp = list(combinations(combi[i],2))
    # print(temp)
    # print(len(temp))
    a_t = []
    for j in range(len(temp)):
        a_t.append(matrix[temp[j][0]][temp[j][1]] + matrix[temp[j][1]][temp[j][0]])
    A.append(sum(a_t))

    #반대
    temp2 = list(combinations(combi[-1-i], 2))
    # print(temp2)
    b_t = []
    for j in range(len(temp)):
        b_t.append(matrix[temp2[j][0]][temp2[j][1]] + matrix[temp2[j][1]][temp2[j][0]])
    B.append(sum(b_t))

# print("A",A)
# print("B",B)

mini = []
for i in range(len(A)):
    mini.append(abs(A[i] - B[i]))

print(min(mini))
