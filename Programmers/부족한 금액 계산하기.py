def solution(price, money, count):
    res = 0
    for i in range(1,count+1):
        res += price*i
    if res >= money:
        answer = res -money
    else:
        answer = 0


    return answer

print(solution(3,20,4))