import sys
sys.stdin = open("input.txt")
def dfs(idx,s):
    global ans
    if ans < s: #더한 값이 커지면 중지(가지치기)
        return
    if idx == N: # 세번 다 돌았을 때 작은값으로 갱신
        ans = min(ans,s)
        return

    for i in range(N):
        if visited[i] == False: # 방문 안했다면
            visited[i] = True # 방문으로 해주기
            dfs(idx+1, s+MAP[idx][i])
            visited[i] = False #리턴한 뒤에 해당 열 체크한거 복구하기


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int,input().split())) for _ in range(N)]
    visited = [False for _ in range(N)] #열 체크
    ans = N*99 #최대로 큰값 넣어주기
    dfs(0,0)

    print("#{} {}".format(tc,ans))