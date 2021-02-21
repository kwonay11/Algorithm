import sys
sys.stdin = open("input.txt")
def num_del(nums):
    N = len(nums)
    for i in range(0, N-1):  # N-1개 반복해야함
        if nums[i] == nums[i + 1]: #둘다 삭제 해야함
            j = i
            for j in range(j,j+2):
                del nums[i]
            # 삭제하고 다시 for문 돌려줘야함
            return num_del(nums)
    return nums

T = 10

for tc in range(1, T+1):
    N, nums = map(list,input().split())
    # ['1', '2', '3', '8', '0', '9', '9', '0', '8', '4']
    num_del(nums)

    print("#{} {}".format(tc,''.join(nums)))

