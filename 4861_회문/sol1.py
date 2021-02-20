import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    words = [list(input())for _ in range(N)] #글자하나하나씩 받아줌

    #회문이 가로일때
    for i in range(N):
        for j in range(N-M+1):
            temp1 = []
            temp2 = []
            result = []
            for k in range(M):
                temp1.append(words[i][j+k]) #행하나에
            temp2.append(temp1[::-1])
            if temp2[0] == temp1:
                print("#{} ".format(tc), end='')
                print(''.join(temp2[0]))
    #회문이 세로일 때
    for i in range(N):
        for j in range(N-M+1):
            temp1 = []
            temp2 = []
            result = []
            for k in range(M):
                temp1.append(words[j+k][i]) #열하나에
            temp2.append(temp1[::-1])
            if temp2[0] == temp1:
                print("#{} ".format(tc), end='')
                print(''.join(temp2[0]))









