import sys
sys.stdin = open("input.txt")
# M = 2 3 1 1
# N까지 도착하면 return
def move(cnt,now):
    global ans
    if now >= ans: # 정류장을 넘어가면 종료
        return
    if cnt >= N-1: # 정류장에 도착하기도 하나 전에
        ans = now
        return

    for i in range(M[cnt]):

        move(cnt+i+1, now+1)


T = int(input())
for tc in range(1, T + 1):
    L = list(map(int, input().split()))
    N = L[0] # 정류장 수
    M = L[1:] # 배터리용량

    ans = N
    move(0, 0)



    print("#{} {}".format(tc,ans-1))