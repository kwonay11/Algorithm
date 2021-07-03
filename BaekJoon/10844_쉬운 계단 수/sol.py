N = int(input())
res = 0
if N == 1:
    print(9)
else:
    res = (2*N - 3) + (2*(N-1)*8)
    print(res%1000000000)
#틀린코드