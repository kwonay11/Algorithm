import sys
sys.stdin = open("input.txt")

T = int(input())
def in_order(i): #중위순회
    global cnt
    if i <= N:
        in_order(2*i) #왼쪽자식
        tree[i] = cnt # 부모노드일 때 카운트 넣어줌
        cnt += 1 #집어 넣는 수 증가
        in_order(2*i+1) #오른쪽 자식

for tc in range(1, T+1):
    N = int(input())
    tree = [0 for _ in range(N+1)] #0부터 N까지 0으로 채운다 인덱스0은 사용 안함 1부터 N까지 사용할 예정

    cnt = 1
    in_order(1)
    # 루트값과 N/2번 노드에 저장된 값을 출력
    print("#{} {} {}".format(tc, tree[1], tree[N//2]))