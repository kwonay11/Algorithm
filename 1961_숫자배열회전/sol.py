import sys
sys.stdin = open('input.txt')

def func(num):
    new_num = []
    for j in range(N): #열 중심
        temp = []
        for i in range(N):
            temp.append(num[i][j])  #temp로 한 열을 다 넣어주고
        temp.reverse()
        new_num.append(temp) #거꾸로한것을 행으로 넣어주다
    return new_num


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    num = []
    # 2차원 배열 받기
    for i in range(N):
        num.append(list(map(int,input().split())))

    list_90 = func(num)
    list_180 = func(list_90)
    list_270 = func(list_180)

    print('#{} '.format(tc))
    for i in range(N):
        print(''.join(list(map(str, list_90[i]))), ''.join(list(map(str, list_180[i]))),
              ''.join(list(map(str, list_270[i]))))