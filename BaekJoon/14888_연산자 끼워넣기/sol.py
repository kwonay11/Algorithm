def oper(indx,num):
    global L
    if indx == N-1:
        L.append(num)
        return

    for i in range(4):
        temp = num
        if o[i] == 0:
            continue
        if i == 0: # +
            num += A[indx+1]
        elif i ==1: # -
            num -= A[indx+1]
        elif i ==2: # *
            num *= A[indx+1]
        else: # //
            if num < 0:
                num = abs(num)//A[indx+1]*-1
            else:
                num //= A[indx+1]
        o[i] -= 1
        oper(indx+1,num)
        o[i] += 1
        num = temp


N = int(input())
A = list(map(int,input().split()))
o = list(map(int,input().split()))

L = []
oper(0,A[0])

print(max(L))
print(min(L))
