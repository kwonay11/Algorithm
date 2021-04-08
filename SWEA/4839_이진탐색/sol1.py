import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    P,A,B = map(int, input().split())
    start = 1
    end = P
    cnt_A = 0
    cnt_B = 0
    #A의 경우
    while True:
        mid = int((start + end) / 2)
        cnt_A += 1
        if mid == A:
            break
        elif mid < A: #중간값이 찾는값보다 크면 시작점으로 치환
            start = mid
        elif mid > A: #중간값이 찾는값보다 작으면 끝점으로 치환
            end = mid

    #B의 경우
    start = 1
    end = P
    while True:
        mid = int((start + end) / 2)
        cnt_B += 1
        if mid == B:
            break
        elif mid < B:
            start = mid
        elif mid > B:
            end = mid
    #카운트값이 크다면 많이 돈 것으로 진것으로 판단. 이긴것을 출력
    result = ''
    if cnt_A < cnt_B:
        result = 'A'
    elif cnt_A > cnt_B:
        result = 'B'
    elif cnt_A == cnt_B:
        result = '0'

    print("#{} {}".format(tc, result))

