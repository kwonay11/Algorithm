import sys
sys.stdin = open("input.txt")


def move(x,y,cnt):
    global num
    if cnt == 8: #8번 돌아가면 종료
        num.add("".join(temp)) # join에서 str로 받아달라해서 MAP원소들을 int형에서 str로 바꿈
        return
    #우
    if y+1 < 4:
        temp[cnt-1] = MAP[x][y+1]
        move(x,y+1,cnt+1)
    #하
    if x+1 < 4:
        temp[cnt-1] = MAP[x+1][y]
        move(x+1,y,cnt+1)
    #상
    if x-1 >= 0:
        temp[cnt-1] = MAP[x-1][y]
        move(x-1,y,cnt+1)
    #좌
    if y-1 >= 0:
        temp[cnt-1] = MAP[x][y - 1]
        move(x,y-1,cnt+1)

T = int(input())

for tc in range(1,T+1):
    MAP = [list(input().split()) for _ in range(4)]
    # 모든 좌표에서 시작
    num = set()
    temp = ['','','','','','','']
    for i in range(4):
        for j in range(4):

            move(i,j,1)


    print("#{} {}".format(tc, len(num)))