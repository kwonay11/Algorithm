def solution(brown, yellow):
    answer = []
    x,y = 0,3
    cal= (brown + 4)//2

    while 1:
        x = cal - y
        if x < y:
            break
        if x >= y: #조건에 맞으면
            if x*y - brown == yellow:
                answer.append(x)
                answer.append(y)

                break

        y += 1
    return answer



print(solution(8,1))