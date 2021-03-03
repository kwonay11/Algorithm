#첫번째 수는 k, 다음 k개의 수는 집합 S에 포함되는 수
# 입력의 마지막줄은 0
import itertools
while True:
    num = list(map(int,input().split()))
    k = num.pop(0) #맨 첫번째 원소를 k로 줌
    if k == 0: #입력의 마지막줄에는 0 하나만 들어옴
        break

    # print(list(itertools.combinations(num, 6)))
    c = list(itertools.combinations(num,6))
    for i in c: #6자리 조합 #조합의 개수만큼 반복문돌려서 출력
        # print(i)
        for j in i:
            print(j,end= ' ')
        print()
    print()





