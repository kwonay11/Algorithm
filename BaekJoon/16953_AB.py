A, B = map(int, input().split())
cnt = 0

while True:
    if A == B:
        cnt += 1
        break
    elif A > B:
        cnt = -1
        break
    if B % 2 == 0:
        B = B//2
        cnt += 1
    elif B % 10 == 1:
        B = B//10
        cnt += 1
    else:
        cnt = -1
        break

print(cnt)