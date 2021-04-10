N, Q = map(int, input().split())
tree = [0 for _ in range(N+1)] #인덱스 N까지 나타내주기 위해서 N+1까지 만들어줌 맨 첫 0 인덱스는 안씀
for i in range(1, Q+1): #i:트리 인덱스(땅번호)
    ground = int(input())
    for
    if sum(tree[1:ground]) == 0:
        tree[ground] = i
        print(tree)
        print(0)
    else:
        # i 인덱스 앞쪽에서 0이 아닌 첫 땅 번호 출력
        for j in range(1, i):
            if tree[j] != 0:
                print(j)
                print(tree)
                continue

