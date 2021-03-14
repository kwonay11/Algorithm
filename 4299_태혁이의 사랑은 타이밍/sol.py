T = int(input())

for tc in range(1, T+1):
    D, H, M = map(int, input().split())
    result = 0
    # if D < 11:
    #     result = -1
    #     print("#{} {}".format(tc, result))
    #
    # elif D >= 11:
    #     if H < 11:
    #         result = -1
    #         print("#{} {}".format(tc, result))
    #         continue
    #     if H == 11 and M < 11 :
    #         result = -1
    #         print("#{} {}".format(tc, result))
    #         continue

    result += (D - 11) * 24 * 60 + (H - 11) * 60 + (M - 11) #일,시,분
    if result < 0 :
        result = -1

    print("#{} {}".format(tc, result))