N, M = map(int, input().split())
set_str = []
for i in range(N):
    set_str.append(input())

in_str = []
result = []
for j in range(M):
    in_str.append(input())
result = list(set(in_str) & set(set_str))
print(len(set(result)))
# print(in_str)
# print(set_str)

###틀렸다