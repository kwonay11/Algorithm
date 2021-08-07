def solution(record):
    #딕셔너리를 사용하여 Enter Change 일때 그에 맞는 닉네임으로 해시의 값을 바꾸면 됩니다
    answer = []
    res = {}
    for i in record:
        temp = i.split()
        if temp[0] == 'Enter' or temp[0] =='Change':
            res[temp[1]] = temp[2] #아이디를 키로 가지고있는 딕셔너리를 닉네임으로 바꾼다.

    for i in record:
        temp = i.split()
        if temp[0] == 'Enter':
            answer.append(res[temp[1]]+"님이 들어왔습니다.")
        elif temp[0] =='Leave':
            answer.append(res[temp[1]]+"님이 나갔습니다.")

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))