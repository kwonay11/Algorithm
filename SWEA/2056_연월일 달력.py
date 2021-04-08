T = int(input())
day_list = [31, 28, 31,30, 31,30, 31, 31, 30, 31, 30, 31]
for tc in range(1,1+T):
    date = input()
    year = int(date[0:4])

    month = int(date[4:6])
    day = int(date[6:8])
    flag = False

    if month < 1 or month > 13:
        print('#{} -1'.format(tc))
        continue
    for i in range(12):
        if month == i+1:
           if day > day_list[i]:
               print('#{} -1'.format(tc))
               flag = True
               continue
    if flag == True:
        continue
#0을 몇자리 수까지 채워줄지 
    year_print = format(year, '04')
    month_print = format(month, '02')
    day_print = format(day, '02')
    print('#{} {}/{}/{}'.format(tc,year_print,month_print,day_print))