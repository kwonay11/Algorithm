import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    N, H = input().split()
    b = format(int(H, 16), 'b')

    print("#{}".format(tc), end=' ')
    cnt = int(N)*4 - len(b)
    for i in range(cnt):
        print(0,end='')
    print(b)