def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1]
        n = commands[i][2] - 1
        new = sorted(array[start:end])

        answer.append(new[n])

    return answer

a = [1, 5, 2, 6, 3, 7, 4]
c =[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(a,c))