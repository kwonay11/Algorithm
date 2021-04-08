import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    str_input = list(map(str,input().split()))

    str1 = []
    str2 = []

    half = int(N /2 - 0.2) #N개가 짝수개이면 half중간보다 하나 전까지 str1에 저장해주고
    #홀수개 이면 중간값까지 str1에 넣어준다
    for i in range(N): #0부터 4 인덱스
        if i <= half: # 0 1 2
            str1.append(str_input[i])
        elif i > half and i < N: #3 4  #홀수개일 때 말썽
            str2.append(str_input[i])


    result = []
    for i in range(N):
        if i%2 == 0:
            result.append(str1.pop(0))
        elif i%2 == 1:
            result.append(str2.pop(0))


    print("#{}".format(tc), *result)

