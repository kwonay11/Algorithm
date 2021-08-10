def solution(priorities, location):
    answer = 0
    order = [0]*len(priorities)
    order[location] = 1

    while 1:
        m = max(priorities)
        num = priorities.pop(0)
        ord = order.pop(0)
        if num >= m and ord == 1:
            answer += 1
            return answer
        if num >= m and ord == 0:
            answer += 1
            continue
        else:
            priorities.append(num)
            order.append(ord)


print(solution([1, 1, 9, 1, 1, 1],0))