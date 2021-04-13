from itertools import permutations
N = int(input())
a =[]
for i in range(1,N+1):
    a.append(i)
b = list(permutations(a, N))
for i in range(len(b)):
    for j in range(N):
       print(b[i][j],end=' ')
    print()
