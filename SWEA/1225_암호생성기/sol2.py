import sys
sys.stdin = open('input.txt')
from collections import deque
#appedleft, popleft 사용가능

for tc in range(1,11):
    N = int(input())
    num = list(map(int,input().split())) #암호받기
    deq = deque(num)

    cnt = 1
    while True:
        temp = deq[0] - cnt
        if temp <= 0: #빼준값이 0보다 작거나 같으면 0으로 셋팅
            temp =0
        cnt += 1 #cnt는 1~5만 가능함
        if cnt == 6: #6이 되었을 때 다음 수를 뺄 cnt는 1로 바꿔줌
            cnt = 1
        deq.popleft() #첫번째 값 빼주기
        deq.append(temp)

        # 마지막 암호 배열은 모두 한 자리 수, 맨마지막은 0일때 break
        if deq[0] <10 and deq[1] <10 and deq[2] <10 and deq[3] <10 and deq[4] <10 and deq[5] <10 and deq[6] <10 and deq[7] == 0 :break


    print('#{} '.format(N),end='')
    print(*deq)