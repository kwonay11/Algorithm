import sys

sys.stdin = open("input.txt")


def Bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


for tc in range(1, 11):

    N = int(input())
    sort_box = list(map(int, input().split()))
    sort_box = Bubble_sort(sort_box)
    for i in range(N):
        sort_box[-1] -= 1
        sort_box[0] += 1
        sort_box = Bubble_sort(sort_box)
    result = sort_box[-1] - sort_box[0]

    print("#{} {}".format(tc, result))

