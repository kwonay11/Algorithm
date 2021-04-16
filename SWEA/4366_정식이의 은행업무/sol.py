import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    two = input()
    three = input()
    n_two = []

    for i in range(len(two)):

        if two[i] == '1':
            temp = '0'
        else:
            temp = '1'

        n_two.append(int(two[:i] + temp + two[i+1:], 2))

    # print(n_two)

    for i in range(len(three)):
        for k in range(3):
            if three[i] != str(k):
                temp = str(k)
                n_three = int(three[:i] + temp + three[i + 1:], 3)
                if n_three in n_two:
                    ans = n_three

    print("#{} {}".format(tc, ans))