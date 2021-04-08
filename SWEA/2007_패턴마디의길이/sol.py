import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,1+T):
    words = list(input())
    temp = [words[0]] #일단 첫번째 문자를 받아서 temp리스트에 넣어준다
    cnt = 1 #cnt는 문자를 몇개 넣었는지 temp안에 있는 개수
    for i in range(1, len(words)): #인덱스 1부터 끝까지 돌면서 비교
        if temp == words[i:i+cnt]:
            break
        temp.append(words[i])
        cnt += 1
    # print(temp)

    print('#{} {}'.format(tc, len(temp)))