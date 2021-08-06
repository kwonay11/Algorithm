def solution(record):
    #해시를 사용하여 Enter Change 일때 그에 맞는 닉네임으로 해시의 값을 바꾸면 됩니다
    answer = []
    res = []
    for i in record:
        temp = i.split()
        res.append(temp)

    for i in range(len(res)):
        for j in range(0, i):
            if res[i][1] == res[j][1]:
                if res[i][0] == 'Change' or res[i][0] == 'Enter':
                    res[j][2] = res[i][2]
                else: #Leave
                    res[i].append(res[j][2])

    for i in range(len(res)):
        if res[i][0] == 'Enter':
            answer.append(res[i][2]+"님이 들어왔습니다.")
        elif res[i][0] == 'Leave':
            answer.append(res[i][2]+"님이 나갔습니다.")


    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))