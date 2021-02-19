import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1,T+1):
    N = int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))
    #배열 값 받음

    #끝에 2가 있는 점 찾아줌
    end = 0
    for i in range(100):
        if arr[99][i] == 2:
            end = i
            break
    x = 99
    y = end
    #1.기본은 위로 직진 x -= 1
    #2.좌.우를 만난다면 방향 틀어 좌.우로 직진
    #3.0을 만난다면 위로 직진
    #4.행이 0이라면 열값을 출력
    flag = False
    while x > 0 :
        flag = False
        if y+1 < 100 and arr[x][y+1] == 1: #만약 y+1이 범위를 넘어가지 않고, 오른쪽으로 갔을 때 1이 존재한다면
            while True:
                y += 1 #오른쪽으로 이동
                if y+1 < 100 and arr[x][y+1] == 1:
                    continue
                else:
                    x -= 1 #오른쪽으로 가고 바로 넘어가면 왼쪽을 봤을때 1이 있으므로 오른쪽으로 갔다가 왼쪽으로 가는 무한루프에 걸림
                    #그래서 오른쪽으로 가지 않는다면 break를 주기 전에 위로 올라가게한다
                    flag = True
                    break

        if y-1 >= 0 and arr[x][y-1] == 1: #왼쪽
            while True:
                y -= 1
                if y-1 >= 0  and arr[x][y-1] == 1: # 계속 왼쪽으로 직진
                    continue
                else:
                # elif arr[x][y - 1] == 0 or y - 1 == -1 :
                    x -= 1
                    flag = True
                    break
        if flag == False:
            x -= 1 #위쪽




    print('#{} {}'.format(tc,y))