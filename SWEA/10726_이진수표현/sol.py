import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    b = format(M, 'b')  # 2진수로 변환
    ans = list(map(int, list(b)))

    ans.reverse()
    print("#{}".format(tc), end=' ')

    if len(ans) >= N:
        cnt = 0
        for k in range(N):
            cnt += ans[k]
        if cnt == N:
            print('ON')
        else:
            print('OFF')

    else:
        print('OFF')




