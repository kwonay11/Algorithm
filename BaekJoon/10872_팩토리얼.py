def factorial(N):
    if N == 0:
        return 1
    else:
        result = N * factorial(N-1)
        return result

N = int(input())
print(factorial(N))

