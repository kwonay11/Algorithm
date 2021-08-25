def pivo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return pivo(num-1) + pivo(num-2)


n = int(input())
print(pivo(n))