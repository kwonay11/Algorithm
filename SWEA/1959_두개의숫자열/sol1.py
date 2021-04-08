import sys
sys.stdin = open("input.txt")

def check(long, short):
    max_value = -987654321
    for i in range(len(long) - len(short) +1):  #M-N+1개만큼 케이스가 발생함
        result=0
        for j in range(len(short)): #길이가 짧은 것만큼 반복
            result += long[i+j]*short[j]

        if max_value < result:
            max_value = result

    return max_value

T = int(input())

#더 긴걸 가만히 두고 작은것을 이동시킨다
for tc in range(1, T+1):
    N,M  = list(map(int, input().split()))

# N은 A의 개수, M은 B의 개수
    A = list(map(int,input().split()))
    B = list(map(int, input().split()))

    if N > M:
        ans = check(A,B)
    else:
        ans = check(B, A)

    print("#{} {}".format(tc, ans))

