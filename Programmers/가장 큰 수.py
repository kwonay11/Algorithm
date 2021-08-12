def solution(numbers):
    answer = ''
    new = []
    for i in range(len(numbers)):
        if len(str(numbers[i])) == 1 or len(str(numbers[i])) == 2:
            a = 3-len(str(numbers[i]))
            new.append([numbers[i]*(10**a),a])
        elif numbers[i] == 1000: #무조건 맨 뒤에
            new.append([numbers[i], -1])
        else:
            new.append([numbers[i], 0])

    new = sorted(new, key=lambda x: (-x[0], -x[1])) #첫번째 인자,두번째인자 순으로 내림차순 정렬
    print(new)
    four = ''
    cnt = 0
    for i in range(len(new)):
        if new[i][1] == 0:
            answer += str(new[i][0])
        if new[i][1] == -1:
            four = '1000'
            cnt += 1
        else:
            answer += str(new[i][0] // 10**new[i][1])
    for i in range(cnt):
        answer += four

    return answer

print(solution([3,34,32]))