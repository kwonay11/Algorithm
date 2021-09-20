def solution(bridge_length, weight, truck_weights):
    answer = 0
    #스택 위에 올라가는거, 스택에서 빼는거 = 시간 +=1
    #스택에 들락날락 -> += 1
    stack = [0]*bridge_length
    time = 0
    while stack:
        time += 1
        stack.pop(0)
        if truck_weights:
            # 스택합과 남은트럭 맨 앞꺼와 더해서 weight 이하라면 뽑아서 스택에 넣는다
            if sum(stack) + truck_weights[0] <= weight:
                stack.append(truck_weights.pop(0))
            else:#아니라면 0넣음
                stack.append(0)
    return time

print(solution(2,10,[7,4,5,6]))