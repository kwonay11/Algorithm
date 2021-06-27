def solution(board, moves):
    answer = 0
    bag = []

    for k in moves:#moves원소안에 있는걸로
        i = k-1 #세로
        for j in range(len(board)): #가로
            # print(i,j)
            if board[j][i] == 0: #0일 땐 넘김
                continue
            else: #0이 아닐때
                bag.append(board[j][i])
                board[j][i] = 0   #0으로 대체해주기
                if len(bag) >= 2:
                    b1 = bag.pop(-1) #맨끝
                    b2 = bag.pop(-1) #두번째 끝

                    if b1 == b2: #앞꺼와 같으면 없애고 카운트
                        answer += 2
                    else:
                        bag.append(b2) #아니면 두번째 끝꺼부터 다시 넣어줌
                        bag.append(b1)
                break #바구니에 넣었으면 다음 moves로 넘김




    return answer

b = [0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]
m = [1,5,3,5,1,2,1,4]

print(solution(b,m))