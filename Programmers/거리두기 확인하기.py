from collections import deque

# 상하좌우 튜플로 고정
D = ((-1,0),(1,0),(0,-1),(0,1))


def bfs(place,row,col):
    visited = [[False for _ in range(5)] for _ in range(5)]
    q = deque()
    # 지금 위치 방문 마킹
    visited[row][col] = True
    # 행,열 좌표, 거리
    q.append((row,col,0))

    while q:#큐가 존재할 때
        curr = q.popleft()

        #거리가 2를 초과했을 때 패스
        if curr[2] > 2:
            continue
        #거리가 0 이 아닐 때 = 자기 자신이 아닐 때와
        #P값을 만났을 떄
        if curr[2] != 0 and place[curr[0]][curr[1]] == 'P':
            return False
        for i in range(4):
            nr = curr[0] + D[i][0]
            nc = curr[1] + D[i][1]
            # 범위 넘으면 패스
            if nr < 0 or nr > 4 or nc < 0 or nc > 4:
                continue
            # 방문한적 있으면 패스
            if visited[nr][nc]:
                continue
            # 이동할 수 없는 경우 패스
            if place[nr][nc] == 'X':
                continue
            #거리두기
            visited[nr][nc] = True
            q.append((nr,nc,curr[2]+1))

    return True

#체크함수 P를 만났을 때 bfs함수 호출
def check(place):
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':
                if bfs(place, r, c) == False:
                    return False
    return True

def solution(places):
    answer = []
    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))