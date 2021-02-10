import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):

    N= int(input())
    num = list(map(int, input().split()))
    #input().split()이면 문자열 형태의 리스트

    min_num = num[0]
    max_num = num[0]
    for i in num:
        if min_num > i:
            min_num = i
        if max_num < i:
            max_num = i

    result = max_num - min_num
    
    print("#{} {} ".format(tc, result))


