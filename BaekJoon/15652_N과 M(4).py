def dfs():
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    for i in range(1, N+1):
        if len(s) > 0:
            if s[-1] > i:
                continue
        s.append(i)
        dfs() #함수호출
        s.pop() # 출력 후 return하고 마지막 원소 비우기

N, M = map(int, input().split())
s = []
dfs()
