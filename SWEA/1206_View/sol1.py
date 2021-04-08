import sys
sys.stdin = open("input.txt")


for tc in range(1, 11):
    N = int(input())
    arr = list(map(int,input().split()))
    count = 0
    #두번째부터 끝에서 두번째까지 반복
    for i in range(2, N-2):
        # 좌우 1,2 만큼 차이 나는것들의 뺄셈 한다
        left1 = arr[i] - arr[i-1]
        left2 = arr[i] - arr[i-2]
        right1 = arr[i] - arr[i+1]
        right2 = arr[i] - arr[i+2]
        #그 값들이 모두 양수라면 최소값을 찾아준다
        if left1 > 0 and left2 > 0 and right1 > 0 and right2 > 0:
            min_arr = []
            min_arr.append(left1)
            min_arr.append(left2)
            min_arr.append(right1)
            min_arr.append(right2)

            min_num = min_arr[0]
            for j in range(4):
                if min_num > min_arr[j]:
                    min_num = min_arr[j]
            count = count + min_num

    print("#{} {} ".format(tc, count))

