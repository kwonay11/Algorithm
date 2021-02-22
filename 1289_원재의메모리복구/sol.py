import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    str1 = list(map(int,input()))
    N = len(str1)
    str2 = [0]*N #0으로 채워진 리스트를 한개 만들어줌

    # print(str1)
    # print(str2)
    cnt = 0

    for i in range(N):
        if str2[i] == str1[i]:
            continue
        elif str2[i] != str1[i]: #같지 않다면 str1의 인덱스 i번째 값으로 끝까지 채운다
            cnt += 1
            j = i
            for j in range(N):
                str2[j] = str1[i]

    #print(str2)


    print("#{} {}".format(tc,cnt))

