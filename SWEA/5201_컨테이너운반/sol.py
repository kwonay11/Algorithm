import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    weight = list(map(int,input().split()))
    truck = list(map(int,input().split()))

    ans = 0
    for i in range(M):
        temp = []
        for j in range(N):
            if truck[i] >= weight[j]: # 무게가 트럭 용량보다 작거나 같으면
                temp.append(weight[j]) #temp에 넣어줌
        if len(temp) != 0: #temp에 한개라도 들어갔을 때
            ans += max(temp) # temp에 들어있는 최대값을 ans에 더해줌
            for j in range(N):   #최대값을 찾아서 0으로 바꾼뒤 반복문에서 나감
                if weight[j] == max(temp):
                    weight[j] = 0
                    break


    print("#{} {}".format(tc, ans))