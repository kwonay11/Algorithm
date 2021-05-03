import math
T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    #조합문제
    answer = math.factorial(M) // (math.factorial(N) * math.factorial(M - N))
    print(answer)