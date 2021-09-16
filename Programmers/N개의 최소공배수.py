from math import gcd
def lcm(x,y):
    return x*y // gcd(x,y)

def solution(arr):
    # 숫자 두개씩을 lcm함수에 넣어서 반환받기
    answer = arr[0]*arr[1]//gcd(arr[0],arr[1])
    for i in range(2,len(arr)):
        answer = lcm(answer,arr[i])

    return answer

print(solution([2,6,8,14]))