import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input()) #테스트케이스의 번호
    num = list(map(int, input().split()))
    score = [0]*101 #점수는 0부터 100
    for i in range(len(num)): #학생수만큼 반복
        score[100-num[i]] += 1 #점수를 인덱스로받아서 1씩올려줌
                               #100이 score[0]에 들어가도록,순서를 거꾸로 받아서 최대값의 인덱스를 구해준다

    max_score = score[0]
    for j in range(1,101):
        if max_score < score[j]:
            max_score = score[j]

    result = 100 - score.index(max_score) #100에서 뺀 이유는 인덱스를 구하면 중복되어있는 수라면 앞에있는값의 인덱스를 추출해주기때문에 거꾸로했다

    print("#{} {}".format(tc, result))


