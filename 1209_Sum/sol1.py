import sys
sys.stdin = open("input.txt")

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for i in range(100):
        temp_arr = list( map(int,input().split()))
        arr.append(temp_arr) #한 행에 한 리스트 형식으로 받아준다


    #행,열 순회
    sum_row = []
    sum_col = []
    for i in range(100):
        sum1,sum2 =0,0
        for j in range(100):
            sum1 += arr[i][j] #행
            sum2 += arr[j][i] #열
        sum_row.append(sum1)  # 행의 합을 리스트로 만들어줌
        sum_col.append(sum2)  # 열의 합을 리스트로

    max_row = sum_row[0]
    max_col = sum_col[0]
    #각 리스트 합의 최대값 찾아줌
    for m in range(1, 100):
        if max_row < sum_row[m]:
            max_row = sum_row[m]
        if max_col < sum_col[m]:
            max_col = sum_col[m]
    #대각선
    sum3, sum4 = 0, 0
    for i in range(100):
        sum3 += arr[i][i] #왼쪽 대각선
        sum4 += arr[i][99-i] #오른쪽 대각선
    #대각선의 최대값
    max_dig = sum3
    if max_dig < sum4:
        max_dig = sum4

    result = 0
    if max_row >= max_col and max_row >= max_dig:
        result = max_row
    if max_col >= max_row and max_col >= max_dig:
        result = max_col
    if max_dig >= max_row and max_dig >= max_col:
        result = max_dig

    print("#{} {}".format(tc, result))


