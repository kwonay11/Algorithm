N, K = map(int, input().split())
coin = []
#[1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
for i in range(N):
    coin.append(int(input()))
cnt = 0
coin.reverse()
for j in coin: #거꾸로 탐색
    cnt += K//j
    K %= j

print(cnt)