T = int(input())

for tc in range(1,T+1):
    D, A, B, F = map(int,input().split())
    time = float(D/ (A + B)) #총 주어진 시간
    result = time * F  #파리가 날아다닌 거리 = 파리의 시속 * 시간
    print('#',end='')
    print(tc,end=' ')
    print('%.10f'%result)