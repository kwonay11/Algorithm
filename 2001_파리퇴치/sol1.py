import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int,input().split())))

    arr_sum = [] #각 네칸의 합을 저장할 리스트
    for i in range(N-M+1): #한칸전까지 범위로 설정
        for j in range(N-M+1):
            sum_result = 0
            for a in range(0,M): #0부터 M-1까지 더해주기
                for b in range(0,M):
                    sum_result += arr[i+a][j+b]

            arr_sum.append(sum_result)

    print("#{} {}".format(tc, max(arr_sum)))

