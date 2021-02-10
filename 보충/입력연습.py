#문자열 1개 입력 받기 => inpjut()
#문자열을 통으로 한줄 가져온다
tmp = input()
print(tmp)

#정수 1개 입력받기 (2가지)
N = int(input())
print(N, type(N))
#정수 여러개 입력 받기(2가지)
# 4 5 6 7 8 9
a, b, c, d, e, f = map(int, input().split())
print(a,b,c,d,e,f)

arr =list(map(int, input().split()))
print(arr)

#한줄로 들어오는 입력쪼개기(문자열 버전, 정수버전)
tmp = list(input())
print(tmp)

tmp = list(map(int, input()))
print(tmp)