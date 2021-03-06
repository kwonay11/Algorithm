def DFS(x, y):
    visited[x][y] = True

    # ㅡㅡㅡif finish가 trueㅡㅡㅡ
    # return
    # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

    # ㅡㅡㅡif x,y가 목표 지점이면ㅡㅡㅡ
    # 1. 답을 저장..전역변수에
    # 2. 전역 변수 finish true
    # 3. return
    # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

    #우
    if y+1 < N and arr[x][y+1] == 1 and visited[x][y+1] == False:
        DFS(x,y+1)
    #하
    if x+1 < N and arr[x][y+1] == 1 and visited[x+1][y] == False:
        DFS(x+1,y)
    #상
    if x-1 >= 0  and arr[x-1][y] == 1 and visited[x-1][y] == False:
        DFS(x-1,y)
    #좌
    if y-1 >= 0 and arr[x-1][y] == 1 and visited[x-1][y] == False:
        DFS(x,y-1)

def BFS(x,y):
    visited =[]
    Q = []
    Q.append([x,y])
    while Q :
        a = Q.pop(0) #첫번째 값 pop
        # 우
        if a[1] + 1 < N and arr[a[0]][a[1] + 1] == 1 and visited[a[0]][a[1] + 1] == False:
            Q.append(x,y+1)
            visited[x][y+1] = True
        # 하
        if a[0]+1 < N and arr[a[0]+1][a[1]] == 1 and visited[a[0]+1][a[1]] == False:
            Q.append(x+1, y)
            visited[x+1][y] = True
        # 상
        if a[0]-1 >= 0 and arr[a[0] - 1][a[1]] == 1 and visited[a[0] - 1][a[1]] == False:
            Q.append(x-1, y)
            visited[x-1][y] = True

        # 좌
        if a[1]- 1 >= 0 and arr[a[0]- 1][a[1]] == 1 and visited[a[0] - 1][a[1]] == False:
            Q.append(x, y - 1)
            visited[x][y - 1] = True









N = int(input()) #배열의 크기
arr = [list(input()) for _ in range(N)] #N*N
visited= [[] for _ in range(N)]
DFS(0,0)
