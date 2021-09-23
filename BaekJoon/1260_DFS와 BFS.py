def dfs(V):
    # 방문처리
    visit[V] = 1
    print(V,end=' ')
    for i in range(1,N+1):
        if visit[i] == 0 and node[V][i] == 1:
            dfs(i)
def bfs(V):
    que = [V]
    visit[V] = 1
    while que:
        front = que.pop(0)
        print(front,end=' ')
        for i in range(1,N+1): #front와 연결된것들 돌면서
            if visit[i] == 0 and node[front][i] == 1:
                visit[i] = 1 #방문처리
                que.append(i)
N,M,V=list(map(int,input().split()))
node = [[0]*(N+1) for _ in range(N+1)]
visit = [0]*(N+1)

for i in range(M):
    a,b = list(map(int,input().split()))
    # 양 방향으로 연결 시켜주기
    node[a][b] = 1
    node[b][a] = 1

dfs(V)
print()
visit = [0]*(N+1)
bfs(V)
