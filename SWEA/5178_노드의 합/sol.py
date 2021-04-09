import sys
sys.stdin = open("input.txt")

# 3 : T
# 5 3 2 : N,M,L
# 4 1 : tree[4] = 1
# 5 2 : tree[5] = 2
# 3 3 : tree[3] = 3
# tree[2] = tree[4] + tree[5]
# tree[1] = tree[2] + tree[3] 인덱스*2 + 인덱스*2+1

T = int(input())

for tc in range(1, T+1):
    # 노드의 개수 N, 리프 노드의 개수 M, 값을 출력할 노드 번호 L
    N, M, L = map(int, input().split())
    # 왼쪽, 오른쪽, 부모
    tree = [[] for _ in range(N+1)] # 노드의 개수+1 만큼 트리를 만듦
    if N%2 ==0:
        tree.append(0)

    #리프노드 개수 만큼 반복문돌려 트리에 넣어줌
    for i in range(M):
        leaf, data = map(int, input().split())
        tree[leaf] = data

    for i in range(N,1,-2):
        tree[i//2] = tree[i//2*2] + tree[i//2*2 +1]

    print("#{} {}".format(tc, tree[L]))