import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N = int(input())
    num = list(map(int,input().split())) #암호받기

    cnt = 1
    while True:
        temp = num[0] - cnt
        if temp <= 0: #빼준값이 0보다 작거나 같으면 0으로 셋팅
            temp =0
        cnt += 1 #cnt는 1~5만 가능함
        if cnt == 6: #6이 되었을 때 다음 수를 뺄 cnt는 1로 바꿔줌
            cnt = 1
        num.pop(0) #첫번째 값 빼주기
        num.append(temp)

        # 마지막 암호 배열은 모두 한 자리 수, 맨마지막은 0일때 break
        if num[0] <10 and num[1] <10 and num[2] <10 and num[3] <10 and num[4] <10 and num[5] <10 and num[6] <10 and num[7] == 0 :break


    print('#{} '.format(N),end='')
    print(*num)