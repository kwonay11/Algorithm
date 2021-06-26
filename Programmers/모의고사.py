s1 = [1, 2, 3, 4, 5]
s2 = [2, 1, 2, 3, 2, 4, 2, 5]
s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]


def solution(answers):
    n1, n2, n3, c1, c2, c3 = 0, 0, 0, 0, 0, 0
    for i in range(len(answers)):

        if c1 == len(s1):
            c1 = 0
        if c2 == len(s2):
            c2 = 0
        if c3 == len(s3):
            c3 = 0

        if s1[c1] == answers[i]:
            n1 += 1
        if s2[c2] == answers[i]:
            n2 += 1
        if s3[c3] == answers[i]:
            n3 += 1
        c1 += 1
        c2 += 1
        c3 += 1

    print(n1,n2,n3)

    answer = []
    if max(n1,n2,n3) == n1:
        answer.append(1)
    if max(n1,n2,n3) == n2:
        answer.append(2)
    if max(n1,n2,n3) == n3:
        answer.append(3)



    return answer

a= [1, 2, 3, 4, 5]
print(solution(a))