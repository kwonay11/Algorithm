num = int(input())
info = []
for i in range(num):
    age,name = input().split()
    info.append([int(age),name])

info = sorted(info, key=lambda x: x[0])
for i in range(num):
    print(info[i][0],info[i][1])

