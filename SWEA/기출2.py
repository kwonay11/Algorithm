T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split()) # N:숫자 목록의 길이 M:탐색횟수를 비교할 숫자의
    b = list(map(int, input().split()))#탐색할 M개의 정수
    a = sorted(list(map(int, input().split())))#정렬된 N개의 숫자 목록

    res = []
    for i in b: #i는 리스트 b안에 있는 것 안에 존재하는 것(찾을 값)
        cnt = 0
        left = 0 # 처음에 왼쪽은 인덱스 0번을 가리킴
        right = n-1 # 처음에 오른쪽은 맨 끝 리스트 인덱스를 가리킴

        while left <= right: # 왼쪽이 오른쪽보다 작거나 같을 때 반복
            mid = (left+right)//2 # 중간값은 (왼+오)//2
            if i == a[mid]: #만약 i가 a의 중간에 있으면
                cnt += 1 #카운트 한번 올려주고
                res.append([a[mid], cnt])
                break   #값을 찾았으므로 중지
            elif i > a[mid]: # i가 중간값보다 크면
                left = mid+1 # 왼쪽을 중간값+1로 하여 다시 탐색
                cnt += 1 #카운트 한번 올려주고


            else: # i가 중간값보다 작다면
                right = mid-1  # 오른쪽을 중간값-1로 하여 다시 탐색
                cnt += 1 #카운트 한번 올려주고



    res.sort(key=lambda x: x[1])

    print("#{} {} {}".format(tc,res[0][0] ,res[0][1]))
