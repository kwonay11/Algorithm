#00000010001101
numbers = list(map(int, input()))

for i in range(0,len(numbers),7):
    ans = 0
    for j in range(6,-1, -1):
        ans += numbers[i+6-j] * (2**j)
        # print(i+7-j,j)
    print(ans)
