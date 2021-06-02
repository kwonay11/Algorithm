n = int(input()) #약수의 개수
#진짜 약수들
num = list(map(int,input().split()))
num.sort()
if n%2 == 0:
    print(num[0]*num[-1])
else:
    print(num[n//2]*num[n//2])


