import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    squre = [[0] * 10 for _ in range(10)] #맨 처음에 10X10인 배열을 0로 채운다

    cnt = 0

    for n in range(N): #색종이 수만큼 반복
        x1,y1,x2,y2,color = map(int, input().split())

        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if color == 1: #빨강
                    if squre[x][y] == 0:
                        squre[x][y] = 1
                    elif squre[x][y] == 2: #파랑으로 채워져있을 때
                        squre[x][y] = 3 #보라로 바꿔준다
                        cnt += 1
                if color == 2: #파랑일 때
                    if squre[x][y] == 0:
                        squre[x][y] = 2
                    elif squre[x][y] == 1: #빨강으로 채워져있을 때
                        squre[x][y] = 3
                        cnt += 1

    print("#{} {}".format(tc, cnt))

