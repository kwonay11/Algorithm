tc = int(input())    #테케
for t in range(tc):
    n = int(input()) #의상 수
    clothes = {}
    # 옷의 종류를 key값으로 받고 딕셔너리에 key값이 없으면 value를 1로 준다. 존재하면 +1
    for i in range(n):
        value, kind = input().split()
        if kind not in clothes:
            clothes[kind] = 1
        else:
            clothes[kind] += 1

    ans = 1
    # 같은 종류의 개수+1를해서 모두 곱하고 아무것도 선택하지 않은경우 1을 빼준다.
    for k, v in clothes.items():
        ans *= (v+1)

    print(ans-1)


