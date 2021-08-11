def solution(scores):
    answer = ''
    for i in range(len(scores)):
        high = max(scores[i])
        low = min(scores[i])
        for j in range(len(scores)):
            if scores[i][j] == scores[j][i]:
                if scores[i][j] == high or scores[i][j] == low:
                    scores[i][j] = -1
    # print(scores)
    for j in range(len(scores)):
        add = 0
        cnt = 0
        for i in range(len(scores)):
            if scores[i][j] != -1:
                add += scores[i][j]
                cnt += 1
        grade = add / cnt
        if grade >= 90:
            answer += 'A'
        elif 80 <= grade < 90:
            answer += 'B'
        elif 70 <= grade < 80:
            answer += 'C'
        elif 50 <= grade < 70:
            answer += 'D'
        else:
            answer +='F'


    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))