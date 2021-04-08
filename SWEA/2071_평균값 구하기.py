T = int(input())

for tc in range(1,T+1):
    num = list(map(int, input().split()))
    sum = 0

    for i in num:
        sum += i
    aver = round(sum/10)
    #round는 반올림함수 ()안에 인자 생략하면 첫째자리에서 반올림


    print('#{} {}'.format(tc,aver))