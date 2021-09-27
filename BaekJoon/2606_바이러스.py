def bfs(V):
    visit[V] = 1
    q = [V]
    cnt = 0
    while q:
        cnt += 1
        front = q.pop(0)
        for i in range(N+1):
            if visit[i] == 0 and matrix[front][i] == 1:
                visit[i] = 1
                q.append(i)

    print(cnt -1)




N = int(input())
matrix = [[0]*(N+1) for _ in range(N+1)]
visit = [0]*(N+1)
line = int(input())
for i in range(line):
    A, B = map(int,input().split())
    matrix[A][B] = matrix[B][A] = 1
bfs(1)
