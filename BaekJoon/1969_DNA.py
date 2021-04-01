N, M = map(int, input().split()) #N = DNA 갯수 M = DNA의 길이
DNA = [list(input())for _ in range(N)]

apb = ['A','C','G','T']
#자리마다 뭐가 많은지 세어줌
max_apb = 0
new_DNA = []

for j in range(M):
    cnt_apb = [0, 0, 0, 0]

    for i in range(N):
        if DNA[i][j] == 'A':
            cnt_apb[0] += 1
        elif DNA[i][j] == 'C':
            cnt_apb[1] += 1
        elif DNA[i][j] == 'G':
            cnt_apb[2] += 1
        elif DNA[i][j] == 'T':
            cnt_apb[3] += 1
    check = 0
    max_apb = max(cnt_apb)
    for i in range(4):
        if check == 0 and cnt_apb[i] == max_apb:
            new_DNA.append(apb[i])
            check = 1 #알파벳 순으로 하기 위해 max갑
print(''.join(new_DNA))

cnt_dif = 0
for i in range(N):
    for j in range(M):
        if DNA[i][j] != new_DNA[j]: #각 dna요소와 같지 않다면 카운트
            cnt_dif += 1

print(cnt_dif)




