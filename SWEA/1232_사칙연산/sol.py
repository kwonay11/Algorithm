import sys
sys.stdin = open("input.txt")
oper = ['+','-','*','/']
def cal(node):
    global result

    if not tree[node][0] in oper:
        return tree[node][0]
    else:
        left = cal(tree[node][1])
        right = cal(tree[node][2])

        if tree[node][0] == '+':
            result = left + right
        elif tree[node][0] == '-':
            result = left - right
        elif tree[node][0] == '*':
            result = left * right
        elif tree[node][0] == '/':
            result = left // right

        return result





T = 10
for tc in range(1, T+1):
    N = int(input())
    # [데이터(수|연산자),왼쪽 자식노드번호, 오른쪽 자식노드번호]
    tree = [[[] for _ in range(3)] for _ in range(N + 1)] #인덱스 1번부터 N번까지 사용하기 위함
    for i in range(N):
        # 1 - 2 3 / 5 65
        node_info = input().split()
        node_num = int(node_info[0])
        node_data = node_info[1]
        #트리에 데이터 넣어주기
        if node_data not in oper: #숫자면 숫자 넣어주기
            tree[node_num][0] = int(node_data)
        else: #연산자이면 데이터 넣어주기
            tree[node_num][0] = node_data

        if len(node_info) == 4:#사칙연산이므로 자식이 둘다 있을 때 넣어준다.
            tree[node_num][1] = int(node_info[2])
            tree[node_num][2] = int(node_info[3])

    # print(tree)
    result = 0
    cal(1)
    print("#{} {}".format(tc, result))