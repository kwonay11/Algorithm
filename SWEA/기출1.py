# run이 2개, triplet이 2개,run 1 tr 1 일 때 베이비 진
T = int(input())
for tc in range(1, T + 1):
    numbers = list(map(int, input())) #숫자 하나씩 정수로 받음
    counter = [0] * 10 # 0부터 9까지 카운트하는 리스트 만들어줌. 초기화 0으로
    for i in range(len(numbers)):
        counter[numbers[i]] += 1 # 카드의 숫자만큼 리스트에 개수를 세서 저장

    run = 0
    triplet = 0
    res = 0
    # run인지 확인하는 반복문
    for i in range(len(counter)):
        if counter[i] >= 3: # 카운트된 카드가 3장이상 존재하면 run이므로 run+=1
            run += 1
            counter[i] -= 3 # 계산 했으니까 3장 빼줌
            if run == 2:  # run이 두개 이면
                res = 1 # 베이비진
                break

    # triplet인지 확인하는 반복문
    for i in range(1,len(counter)-1):
        if counter[i] == 1: # 연속된 숫자 가운데 숫자카드가 1개 존재하면
            if counter[i-1] == 1 and counter[i+1] == 1:# 전,후 숫자 카드가 1개 존재 해야 triplet
                triplet += 1
                counter[i] -= 1 # 계산했으니까 1장 빼줌
                if triplet == 2: # triplet이 두개이면
                    res = 1 # 베이비 진
                    break
        if counter[i] == 2: #예를 들어 카드가 123123일 때 triplet이 2개가 가능 하므로 베이비진
            if counter[i - 1] == 2 and counter[i + 1] == 2:
                res = 1
                break
    if run == 1 and triplet == 1: # run한개 triplet 1개 이면
        res = 1 # 베이비진

    print("#{} {}".format(tc, res))



