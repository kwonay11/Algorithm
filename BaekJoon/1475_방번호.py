#6 <=> 9

N = list(map(int, input()))

cnt_list = [0] * 10
#배열의 인덱스와 같은 곳에 카운트 해주기
for i in range(len(N)):
    check = N.pop(0)
    cnt_list[check] += 1

# (6횟수 + 9횟수 + 1 )//2해서 6번에 넣어준다
# 9번은 0으로 바꿔줌
cnt_list[6] = (cnt_list[6]+cnt_list[9]+1)//2
cnt_list[9] = 0

#최대값 출력
print(max(cnt_list))


#처음 0-9까지는 set_cnt = 1, 중복된게 있다면 set_cnt += 1


# set_cnt, cnt_9, cnt_6 = 1, 0, 0
# check_list = []
# while N:
#     check = N.pop(0) # 맨 앞에 뽑음
#     if check in check_list: #먼저 뽑았던거와 같은게 있으면 세트 카운트
#         set_cnt += 1
#         # print(check, set_cnt)
#     if check == '9':
#         cnt_9 += 1
#     elif check == '6':
#         cnt_6 += 1
#     check_list.append(check)
# print('전체 카운트:',set_cnt)
#
# # 개수가 같을 때
# if set_cnt-cnt_6< cnt_6 or set_cnt-cnt_9 < cnt_9:
#     if cnt_9 != 0 and cnt_6 != 0 and cnt_9 == cnt_6:
#         set_cnt = cnt_6
#
#
#     #모두 9일 때, 모두 6일 때
#     if cnt_6 == 0 and cnt_9 == set_cnt:
#         set_cnt //= 2
#
#     if cnt_9 == 0 and cnt_6 == set_cnt:
#         set_cnt //= 2
#
#
#
#     #9와 6이 둘다 있을 때 적게 있는 개수를 전체에서 뺀다
#     if cnt_9 != 0 and cnt_6 > cnt_9:
#         set_cnt -= cnt_9
#         # set_cnt += 1
#     elif cnt_6 != 0 and cnt_6 < cnt_9:
#         set_cnt -= cnt_6
#         # set_cnt += 1
#
#
# print(set_cnt)