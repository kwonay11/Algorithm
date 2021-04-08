import sys
sys.stdin = open('input.txt')
#가로를 계산하는 경우: 시작하는곳 왼쪽에는 0이거나 퍼즐의 첫 부분이어야한다.
#즉, 왼쪽은 1이 아님
#세로로 계산하는 경우: 위가 0이거나 퍼즐의 끝부분 이어야한다
#즉, 위쪽은 1이 아님
#가로는 오른쪽으로 갔을 때 K칸만큼 1이 갔으면 K+1칸은 1이면 안됨
#세로는 아래로 갔을 때 K칸만큼 1이 갔으면 K+1칸은 1이면 안됨

T = int(input())

for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    #배열 받기
    result = 0
    cnt = 0
    #가로를 봤을 때
    for x in range(N):
        #행(x) 기준으로 하기
        for y in range(N):
            if arr[x][y] == 1:
                cnt += 1
            if arr[x][y] == 0 or y == N-1: # 0을 만났거나 벽을 만났을 때
                if cnt == K: # 이전에 계산한 카운트가 k라면 result에 카운트
                    result += 1
                cnt = 0 #카운트 초기화

#세로를 봤을때

    for y in range(N):
        #열(y)기준으로 보기
        for x in range(N):
            if arr[x][y] == 1: #1이면 카운트
                cnt += 1
            if arr[x][y] == 0 or x == N-1 :  # 0을 만났거나 벽을 만났을 때
                if cnt == K:   # 이전에 계산한 카운트가 k라면 result에 카운트
                    result += 1
                cnt = 0



    print('#{} {}'.format(tc,result ))