T = int(input())
for tc in range(1, T+1):
    N,M = list(map(int,input().split()))
    nums = list(map(int,input().split())) #N개 숫자

    for i in range(M): #M번 이동
        temp = nums.pop(0) #맨 앞 빼서 맨뒤로보낸다
        nums.append(temp)

    print('#{} {}'.format(tc,nums.pop(0)))