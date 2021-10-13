import sys
input = sys.stdin.readline
from collections import deque
#rotate는 deque에서만 가능

N,K = map(int,input().split())
belt = deque(map(int,input().split()))

robot = deque([0]*N)
cnt = 1


while 1:
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0 #내려가는 위치 로봇 삭제


    #로봇이 있을 때 다음 칸으로 이동

    for i in range(N-2,-1,-1):
        #다음로봇은 없고 벨트내구도 1이상일 때
        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >= 1:
            robot[i+1] = 1
            robot[i] = 0
            belt[i+1] -= 1
    robot[-1] = 0
    # 로봇을 올릴 때
    if belt[0] >= 1 and robot[0] == 0:
        robot[0] = 1
        belt[0] -= 1


    # 0이 K개 이상이면 종료
    if belt.count(0) >= K:
        print(cnt)
        break
    cnt += 1


