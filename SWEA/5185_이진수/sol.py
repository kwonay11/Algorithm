import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    N, H = input().split()
    b = format(int(H, 16), 'b') # 16진수로 들어온것을 10진수로 표현한 수를 다시 2진수로 바꿔준

    print("#{}".format(tc), end=' ')
    cnt = int(N)*4 - len(b) #2진수는 4자리수로 나타나야 함
    for i in range(cnt):
        print(0,end='')
    print(b)