def solution(s):
    answer = []
    res = 0
    temp = []
    check = False
    n = []
    num = 1

    for k in range(1,len(s)-1):
        if s[0] == s[k]:
            check = True
            n.append(k) #거리 배열 생성해주기
    #print(n)
    if len(n) == 0: #맨 첫 원소가 반복되지 않는다면 그 문자열 개수 리턴
        return len(s)


    for i in n:
        answer = []
        currentStr = s[0:i]
        # print(currentStr)
        for j in range(i,len(s), i): #거리만큼 떨어트려서 반복
            ###남는 문자열이 단위보다 작으면 예외처리
            if currentStr == s[j:j+i]: #반복한다면
                num += 1
            else: #반복하지 않다면
                #print(num, " : ", currentStr)
                if num != 1:
                    answer.append(num)
                answer.append(currentStr)
                num = 1 #초기화
                currentStr = s[j:j+i]
        if num != 1:
            answer.append(num)
        answer.append(currentStr)
        num = 1  # 초기화

        # ('').join(answer)
        temp.append(answer)
        #print(temp)

    result = []
    for i in range(len(temp)):
        dis = 0
        for j in range(len(temp[i])):
            dis += len(str(temp[i][j]))
        result.append(dis)

    answer = min(result)



    return answer

a = "aabbaccc"
print(solution(a))
#solution(a)