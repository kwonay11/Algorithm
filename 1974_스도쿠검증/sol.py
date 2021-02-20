import sys
sys.stdin = open('input.txt')

T = int(input())
check = [1,2,3,4,5,6,7,8,9] #스도쿠 검증 리스트
for tc in range(1,T+1):
    arr = []
    row_cnt = [0] * 9
    for i in range(9):
        temp = []
        temp = list(map(int,input().split()))
        if sorted(temp) == check:
            row_cnt[i] = 1 #행에 스도쿠 가능한지 확인
        arr.append(temp)
    #print(arr) #배열 잘 받았는지 확인
    #print(row_cnt)
    col_cnt = [0]*9
    for j in range(9): #열 중심
        temp1 = 0
        for i in range(9):
            temp1 += arr[i][j]
        if temp1 == 45:
            col_cnt[j] = 1
    #print(col_cnt)

    sum1 = 0
    squre_cnt = [0] * 9
    a = 0
    b = 0
    cnt = 0
    for i in range(a,9,a+3):
        for j in range(b,9,b+3): #정사각형
            for x in range(i,i+3):
                for y in range(j,j+3):
                    sum1 += arr[x][y]
                if sum1 == 45:
                    squre_cnt[cnt] = 1
        cnt += 1

    #print(squre_cnt)
    result = 0
    for i in range(9): #row_cnt, col_cnt 안에 있는 리스트 요소들이 모두 다 1이어야 하므로 더해서 18일때만 사각형안의 조건을 봐준다
        if sum(row_cnt) + sum(col_cnt) == 18 and squre_cnt[i] == 1:
            result = 1

    print('#{} {}'.format(tc, result))