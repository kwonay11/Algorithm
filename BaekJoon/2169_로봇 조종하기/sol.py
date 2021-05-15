def DFS(x,y,cnt):
    global res
    if x == N-1 and y == M-1:
        if res < cnt:
            res = cnt
        return
    if x+1 < N and visited[x+1][y] == False:# 오른쪽
        visited[x + 1][y] = True
        DFS(x+1,y,MAP[x+1][y] +cnt)
        visited[x + 1][y] = False
    if x-1 >= 0 and visited[x-1][y] == False:# 왼쪽
        visited[x - 1][y] = True
        DFS(x-1,y,MAP[x-1][y] +cnt)
        visited[x - 1][y] = False
    if y+1 < N and visited[x][y+1] == False:# 아랫쪽
        visited[x][y+1] = True
        DFS(x,y+1,MAP[x][y+1] +cnt)
        visited[x][y + 1] = False

# 0,0부터 N-1,N-1까지
N, M = map(int,input().split())
MAP = [list(map(int,input().split()))for _ in range(N)]
# print(MAP)
visited = [[False]*N for _ in range(M)]

res = 0
DFS(0,0,MAP[0][0])
print(res)
print(visited)

