T = int(input())
month = [0 ,31,28,31,30,31,31,30,31,30,31]

days = [0] * 13 #각 달까지의 모든 날짜
for i in range(1, len(days)) :
    days[i] = days[i-1] + month[i]

for tc in range(1, T+1):
    m1,d1,m2,d2 = map(int , input().split())
    #전달까지의 모든날짜 + 이번날짜
    first = days[m1-1] +d1
    second = days[m2-1] + d2

    print("#{} {}" .format(tc, second-first+1))

