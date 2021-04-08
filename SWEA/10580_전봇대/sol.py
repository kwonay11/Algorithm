import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    lst = [list(map(int, input().split())) for i in range(N)]
    #교차하는 케이스는 2개
    #A1<A2 이고 Y1>Y2일 때 교차
    #A1>A2 이고 Y1<Y2일 때 교차
    for i in range(N):
        for j in range(N):
            if lst[i][0] < lst[j][0]:
                if lst[i][1] > lst[j][1]:
                    cnt += 1
            elif lst[i][0] > lst[j][0]:
                if lst[i][1] < lst[j][1]:
                    cnt += 1
##########행렬로 했더니 런타임에러###########
    # N = int(input())
    # cnt = 0
    # arr = [[0] * 10000 for _ in range(10001)]
    # for i in range(N):
    #     A, B = map(int, input().split())
    #     # A는 고정이고 B만 바꾸면 됨 = 행 고정
    #     for b in range(1, B + 1):
    #         arr[A][b] = 1
    #     for b in range(1, B + 1):
    #         if b == A:
    #             cnt -= 1
    #
    #         if arr[b][A] == 1:
    #             cnt += 1

    print('#{} {}'.format(tc, cnt))




    print('#{} {}'.format(tc, cnt//2))