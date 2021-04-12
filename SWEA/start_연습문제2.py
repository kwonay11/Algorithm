#0F97A3
h = int(input(),16) #16진수로 받기

b = format(h, 'b') #2진수로 변환
# print(list(b))
ans = []
for i in range(0,len(b),7):
    temp =[]
    for j in range(7):
        temp.append(int(b[i+j]))
    ans.append(temp)
print(ans)
# [[1, 1, 1, 1, 1, 0], [1, 0, 1, 1, 1, 1], [1, 0, 0, 0, 1, 1]]

for i in range(len(b)//7):
    result = 0
    for j in range(6,-1, -1):
        result += ans[i][6-j] * (2**j)
        # print(i+7-j,j)
    print(result)