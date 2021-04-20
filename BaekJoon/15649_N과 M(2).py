def dfs():
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    for i in range(1, N+1):
        if i in s: # 가지치기, 이미 선택한 숫자 배제
            continue
        if len(s) > 0:
            if s[-1] > i:
                continue
        s.append(i)
        dfs() #함수호출
        s.pop() # 출력 후 return하고 마지막 원소 비우기

N, M = map(int, input().split())
s = []
dfs()
