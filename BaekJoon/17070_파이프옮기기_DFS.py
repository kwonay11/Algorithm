# 벽만났을 때
# import sys
# sys.stdin = open('input.txt')


def move(x, y, shape): #shape :1가로 2:세로 3:대각선
    global cnt

    if x == N-1 and y == N-1:
        cnt += 1
        return

    if shape == 1: #가로라면
        if y+1 <= N-1 and squre[x][y+1] == 0: #가로
            move(x, y+1, 1)
        if x+1 <= N-1 and y+1 <= N-1 and squre[x+1][y] == 0 and squre[x][y+1] == 0 and squre[x+1][y+1] == 0: #대각선
            move(x+1, y+1, 3)
    elif shape == 2: #세로라면
        if x+1 <= N-1 and squre[x+1][y] == 0: #세로
            move(x+1, y, 2)
        if x+1 <= N-1 and y+1 <= N-1 and squre[x+1][y] == 0 and squre[x][y+1] == 0 and squre[x+1][y+1] == 0: #대각선
            move(x+1, y+1, 3)
    elif shape == 3: #대각선이라면
        if y+1 <= N-1 and squre[x][y+1] == 0: #가로
            move(x, y+1, 1)
        if x+1 <= N-1 and squre[x+1][y] == 0: #세로
            move(x+1, y, 2)
        if x+1 <= N-1 and y+1 <= N-1 and squre[x+1][y] == 0 and squre[x][y+1] == 0 and squre[x+1][y+1] == 0: #대각선
            move(x+1, y+1, 3)




N = int(input())

squre = [list(map(int, input().split(' ')))for _ in range(N)]

cnt = 0
move(0, 1, 1) #처음은 항상 가로 파이프는 (0,0)과 (0,1)에 걸쳐져 있다

print(cnt)

