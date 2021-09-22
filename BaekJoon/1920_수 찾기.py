N=int(input())
A=list(map(int,input().split()))
M = int(input())
B=list(map(int,input().split()))

for num in B:
    if num in A:
        print(1)
    else:
        print(0)