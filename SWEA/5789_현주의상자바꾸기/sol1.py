import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N, Q = map(int,input().split())
    num = [0] * N #처음은 N개의 0
    for i in range(1, Q+1):
        L, R = map(int,input().split())
        #L번부터 R번까지 상자의 값을 i로 변경
        for j in range(L-1, R):
            num[j] = i
    print("#{}".format(tc), end=' ')
    print(*num)

