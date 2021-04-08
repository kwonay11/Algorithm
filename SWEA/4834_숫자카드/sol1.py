import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    #카드 장수 : N
    N =int(input())
    card = list(input())
    #카운트 리스트 10개 생성
    count = [0] * 10

    for i in range(N):
        count[int(card[i])] += 1

    max_count = 0

    #큰 숫자 저장 리스트
    idx =[0]
    #카운트가 최고이면 idx리스트에 추가하고 
    #최고카운트와 카운트값이 같으면 그 숫자를 idx리스트안에  뒤에 붙여준다
    for j in range(len(count)):
        if max_count <= count[j]:
            max_count = count[j]
            idx.append(j)
      


    print("#{} {} {} ".format(tc,idx.pop(),max_count ))

