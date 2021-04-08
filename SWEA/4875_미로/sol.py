import sys
sys.stdin = open("input.txt")

def func(i, j):
    global result
    visited[i][j] = 1
    # print(i, j,nums[i][j])

    if nums[i][j] == 3: #값이 안들어감
        # print(i, j)
        result = 1
        return

    if i-1 >= 0 and nums[i-1][j] != 1 and visited[i-1][j] == 0:#
        func(i-1, j)
        if result == 1:
            return
    if j-1 >= 0 and nums[i][j-1] != 1 and visited[i][j-1] == 0:# 좌
        func(i, j - 1)
        if result == 1:
            return
    if j+1 < N and nums[i][j+1] != 1 and visited[i][j+1] == 0: #우
        func(i, j + 1)
        if result == 1:
            return
    if i+1 < N and nums[i+1][j] != 1 and visited[i+1][j] == 0: #하
        func(i+1, j)
        if result == 1:
            return







T = int(input())

for tc in range(1,T+1):
    N = int(input())
    nums = [list(map(int,input())) for _ in range(N)]

    ###입력 완료
    start = 0
    for x in range(N):
        for y in range(N):
            if nums[x][y] == 2:
                s_x = x
                s_y = y


    result = 0
    visited = [[0]*(N) for _ in range(N)]

    func(s_x, s_y)


    print('#{} {}'.format(tc,result))