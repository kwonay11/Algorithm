import sys

N = int(sys.stdin.readline())
nums = []
for i in range(N):
    li= sys.stdin.readline().split()

    if li[0] == 'push':
        nums.append(li[1])
    elif li[0] == 'pop':
        if len(nums) == 0:
            print(-1)
        else:
            print(nums.pop())
    elif li[0] == 'size':
        print(len(nums))
    elif li[0] == 'empty':
        if len(nums) == 0:
            print(1)
        else:
            print(0)
    elif li[0] == 'top':
        if len(nums) == 0:
            print(-1)
        else:
            print(nums[-1])
