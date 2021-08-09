def solution(number, k):
    answer = ''
    res = []
    for i in number:
        # 스택안에 숫자가 있고, 들어온 숫자가 스택안에 마지막 숫자보다 크고 제거할 숫자가 남았을 때
        while res and i > res[-1] and k > 0:
            res.pop() #맨뒤 빼고
            k -= 1  #카운트 하나 감소
        res.append(i) #숫자 넣음


    return "".join(res[:len(res)-k])

print(solution("4177252841",4))