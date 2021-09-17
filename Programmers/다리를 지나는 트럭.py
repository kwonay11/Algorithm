def solution(bridge_length, weight, truck_weights):
    answer = 0
    #스택 위에 올라가는거, 스택에서 빼는거 = 시간 +=1
    stack = []
    time = 0

    for i in range(len(truck_weights)):
        num = truck_weights.pop(0)
        stack.append(num)
        time += 1
        if sum(stack) > weight:
            num2 = stack.pop()
            truck_weights.insert(0,num2)
            time += (len(stack)+1)
            stack = []


        if len(stack) == bridge_length:
            stack = []
            time += bridge_length


    return time

print(solution(2,10,[7,4,5,6]))