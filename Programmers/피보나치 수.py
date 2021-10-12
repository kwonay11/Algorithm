def solution(n):
    answer = 0
    n1,n2 = 1,1
    if n == 2:
        return 1
    else:
        for i in range(3,n+1):
            answer = (n1 + n2)%1234567
            n1 = n2
            n2 = answer
        return answer




print(solution(5))