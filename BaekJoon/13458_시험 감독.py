N = int(input())
Ai = list(map(int,input().split()))
B, C = map(int,input().split())
#처음에 총감독 다 들어감
answer = N

for a in Ai:
    a -= B
    if a > 0:
        if a%C: #나머지가 있으면
            answer += (a//C)+ 1
        else:
            answer += (a//C)
print(answer)

