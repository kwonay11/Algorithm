import sys
sys.stdin = open("input.txt")


def in_order(node): #중위순회
    if tree[node][3] != 0:# 부모노드값이 들어있으면
        in_order(tree[node][0]) #왼쪽 자식
        print(tree[node][3], end='') #부모데이터 출력
        in_order(tree[node][1]) #오른쪽 자식

T = 10
for tc in range(1, T+1):
    N = int(input())
    #왼쪽자식,오른쪽 자식,부모,데이터
    tree = [[0 for _ in range(4)] for _ in range(N + 1)]
    #처음에 트리를 0으로 다 채워 놓는다
    for i in range(N):
        # 1 W 2 3 / 8 S
        node_info = input().split()
        node_num = int(node_info[0])
        node_data = node_info[1]
        #트리에 데이터 넣어주기
        tree[node_num][3] = node_data

        #왼쪽 자식 여부 판단
        if node_num * 2 <= N:
            tree[node_num][0] = int(node_info[2])
            #오른쪽 자식 여부 판단
            if node_num * 2 + 1 <= N:
                tree[node_num][1] = int(node_info[3])
    print('#{}'.format(tc), end=' ')
    in_order(1)
    print()





