import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    arr = input()
    N =len(arr)
    stack1 = []
    result = 1
    left = 0
    right = 0
    #왼쪽괄호들을 다 스택에 저장하고 오른쪽 괄호를 만난다면 pop해서 비교
    for i in range(N):
        if arr[i] == '(' or arr[i] == '{':
            stack1.append(arr[i])
            left += 1
        if arr[i] == ')':
            right += 1
            if len(stack1) > 0 and stack1.pop() != '(':
                result = 0
                break
        elif arr[i] == '}':
            right += 1
            if len(stack1) > 0 and stack1.pop() != '{':
                result = 0
                break
    if len(stack1) != 0: #스택에 비워지지 않았다면 왼쪽 괄호가 더 많은 것이므로 0
        result = 0

    if left != right:
        result = 0

    print("#{} {}".format(tc,result ))




