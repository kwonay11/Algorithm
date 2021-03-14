import sys
sys.stdin = open('input.txt')

def hamburger(indx, sum_favor, sum_kcal):
    global best
    if sum_kcal > L: #정해진 칼로리를 넘으면 return
        return
    if sum_favor > best: #최고 갱신
        best = sum_favor
    if indx == N: #갯수 다 돌았으면 리턴
        return


    hamburger(indx+1, sum_favor + f_k[indx][0], sum_kcal + f_k[indx][1]) #선택한 경우
    hamburger(indx + 1, sum_favor, sum_kcal) #선택하지 않은 경우 다음 번째 항목으로 넘김


T = int(input())

for tc in range(1, T+1):

    N, L = map(int, input().split()) #5 1000

    f_k = [list(map(int, input().split()))for _ in range(N)] # 맛점수, 칼로리 점수 리스트로 들어옴

    #favor_k = [[100 200],[300 500], [250 300], [500 1000], [400 400]]

    best = 0  #최고점 초기화
    hamburger(0, 0, 0)
    print("#{} {}".format(tc, best))