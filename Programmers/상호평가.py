def solution(scores):
    answer = ''
    for j in range(len(scores)):
        cnt = len(scores)
        add = 0
        high = 0
        low = 101
        for i in range(len(scores)):
            add += scores[i][j]
            if i == j:
                continue
            if high < scores[i][j]:
                high = scores[i][j]
            elif low > scores[i][j]:
                low = scores[i][j]

        if scores[j][j] > high or scores[j][j] < low:
            add -= scores[j][j]
            cnt -= 1
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
            answer += 'F'

    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))