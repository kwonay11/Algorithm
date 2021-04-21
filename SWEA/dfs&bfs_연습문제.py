# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
#트리로 표현하기
def dfs(num):
    visited[num] = True
    print(num, end='-')
    for i in range(len(tree[num])):
        if visited[tree[num][i]] == False:
            dfs(tree[num][i])
def bfs(num):
    Q = [num]
    visited[num] = True
    while Q:
        n = Q.pop(0)
        print(n, end='-')
        for i in range(len(tree[n])):
            if visited[tree[n][i]] == False:
                Q.append(tree[n][i])
                visited[tree[n][i]] = True


L = list(map(int,input().split()))
tree = [[] for _ in range((len(L)//2))]

for i in range(0, len(L),2):
    a = L[i]
    b = L[i+1]
    tree[a].append(b)
    tree[b].append(a)

# print(tree)
visited = [False] * ((len(L)//2)+1)
# print(visited)
dfs(1)
#bfs(1)

