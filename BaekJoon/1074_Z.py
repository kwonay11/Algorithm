cnt = 0
def func(a,x,y):
    global cnt
    if a == 2:
        if x == r and y == c: #왼쪽 위
            print(cnt)
            return
        cnt += 1
        if x == r and y + 1 == c: #오른쪽 위
            print(cnt)
            return
        cnt += 1
        if x+1 == r and y == c: # 왼쪽아래
            print(cnt)
            return
        cnt += 1
        if x+1 == r and y+1 == c: #오른쪽 아래
            print(cnt)
            return
        cnt += 1
    else:
        func(a//2, x, y)# 첫번째 사각형(왼쪽 위)
        func(a//2,x, y + a//2) #두번째 (오른쪽 위)
        func(a // 2, x + a //2, y )  # 세번째(왼쪽 아래)
        func(a // 2, x + a // 2, y + a // 2)  # 네번째 (오른쪽 아래)




N, r, c = map(int,input().split())
num = 2**N #num은 한변의 길이
func(num,0,0)
#좌표 r,c에 있는 cnt수를 출력해야한다.