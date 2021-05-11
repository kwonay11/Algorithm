piece = list(input().split())
temp = 0
while(1):
    if sorted(piece) == piece:
        break
    for i in range(len(piece)-1):
        if piece[i] > piece[i+1]:
            temp = piece[i]
            piece[i] = piece[i+1]
            piece[i+1] = temp
            print(*piece)

