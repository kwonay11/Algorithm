# n이 홀수이면 목표 기둥에 시작할 원반을 놓는다.
# n이 짝수이면 otehr기둥에 시작할 원반을 먼저 놓는다.
##제일 큰 원반을 목표기둥에 쌓게하고 1부터 n-1까지의 원반은 other기둥에 쌓이게 한다.
#n-1까지의 원판이 other기둥에 있는데 이것들을 목표 기둥에 넣어주려면 위의 과정과 같다, other에서 시작하고 end가 목표로.

def hanoi(n,start,end,other): #함수인자 순서 처음넣는기둥,목표기둥, 나머지 기둥

    if n == 1:
        print(start, end)
        return #맨 위꺼 목표기둥에 쌓으면 종료

    hanoi(n-1, start, other, end) #제일 큰 원판을 목표기둥에 쌓는다
    print(start,end)
    hanoi(n-1, other, end, start) # n-1까지의 원판이 목표기둥에 쌓인다



N = int(input()) #3
k = 2**N -1 #7
print(k)
hanoi(N,1,3,2)
