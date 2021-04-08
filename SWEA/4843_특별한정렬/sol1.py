import sys
sys.stdin = open("input.txt")

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    bubble_sort(arr)

    new_list1 = [] #큰 수 리스트로 담기
    new_list2 = [] #작은수
    for i in range(0, len(arr)//2):
            new_list2.append(arr[i])
    for i in range(len(arr)-1, (len(arr)//2)-1, -1): #큰수는 거꾸로 담기
        new_list1.append(arr[i])

    # print('list1',new_list1)
    # print('list2',new_list2)

    print("#{} ".format(tc),end='')
    for j in range(0,10): #10개만 출력
        if j%2 == 0: #짝수면 큰거 출력
            print(new_list1.pop(0),end= ' ')
        elif j% 2 == 1:
            print(new_list2.pop(0),end= ' ')
    print('')



    


