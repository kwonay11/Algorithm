S = list(input())
T = list(input())
ans = 0
while T:
    if S == T:
        ans = 1
        break
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T.reverse()
print(ans)
