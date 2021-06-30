def solution(s):
    s = list(map(int, s.split(' ')))
    return '{} {}'.format(min(s), max(s))

a = "1 -2 -3 -4"
print(solution(a))
