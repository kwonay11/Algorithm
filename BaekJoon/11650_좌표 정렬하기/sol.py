N = int(input())
list = []
for tc in range(N):
    x,y = map(int,input().split())
    list.append([x,y])
# print(list)
list.sort(key = lambda x : (x[0],x[1]))
for i in range(N):
    print(list[i][0],list[i][1])
