##########런타임에러#########
T = int(input())
for tc in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    ans = 0

    while len(lst) > 1:
        M = max(lst) #최고가,갱신
        idx = lst.index(M)
        if idx == 0:
            lst.pop(0)
            continue
        sum_idx = 0
        for i in range(idx):
            sum_idx += lst[i]

        ans += M * idx - sum_idx
        # 제거해주기
        for i in range(idx):
            lst.pop(i)
        lst.pop(0)

    print(ans)
