N = int(input())
room = [list(map(int, input().split()))for _ in range(N)]

#끝나는 시간,시작시간을 기준으로 정렬
room.sort(key=lambda x : (x[1],x[0]))
print(room)
cnt = 1
end = room[0][1] #맨 처음꺼 뽑음

#다음 시작이 앞의 끝나는 시간안에 있으면 삭제
for i in range(1,N):

    if room[i][0] >= end:
        cnt += 1
        # print(room[i])
        end = room[i][1] #갱신

print(cnt)