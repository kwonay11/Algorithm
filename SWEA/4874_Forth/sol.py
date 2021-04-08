import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    str_input = list(input().split())
    result = []

    print('#{}'.format(tc),end=' ')

    for i in range(len(str_input)):
        if str_input[i].isdigit() == True:
            result.append(int(str_input[i]))
        if str_input[i] == '.':
            if len(result) != 1:
                print('error')
                break
            print(result.pop())
            break
        if str_input[i] == '+' :
            if len(result) == 1 or len(result) == 0:
                print('error')
                break
            result.append(result.pop(-2) + result.pop(-1))
        elif str_input[i] == '-':
            if len(result) == 1 or len(result) == 0:
                print('error')
                break
            result.append(result.pop(-2) - result.pop(-1))
        elif str_input[i] == '*':
            if len(result) == 1 or len(result) == 0:
                print('error')
                break
            result.append(result.pop(-2) * result.pop(-1))
        elif str_input[i] == '/':
            if len(result) == 1 or len(result) == 0:
                print('error')
                break
            result.append(result.pop(-2) // result.pop(-1))



