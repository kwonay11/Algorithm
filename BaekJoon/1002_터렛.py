T = int(input())
for tc in range(1, T+1):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dis = 0
    dis = (abs(x1-x2)**2 + abs(y1-y2)**2)**0.5
    # print(dis)
    if x1 == x2 and y1 == y2:
        if r1 != r2: #동심원
            # print("check4")
            print(0)
            continue
        elif r1 == r2: #동일할 때
            # print("check5")
            print(-1)
            continue
    if abs(r1-r2) < dis < r1+r2: #두점
        # print("check1")
        print(2)
        continue
    if r1+r2 == dis or abs(r1-r2) == dis: #외접, 내접
        # print("check2")
        print(1)
        continue
    if r1+r2 < dis or abs(r1-r2) > dis: # 외부에 있을 때, 내부에 있을 때
        #print("check3")
        print(0)
        continue
