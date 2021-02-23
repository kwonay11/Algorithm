import sys
sys.stdin = open("input.txt")

def stack_pop(words):
    for i in range(len(words)-1): #인덱스 0부터 5까지
        if words[i] == words[i+1]:
            j = i

            for j in range(j,j+2): #연속된 두개 삭제
                words.pop(i)
            return stack_pop(words) #재귀
    return len(words)



T = int(input())

for tc in range(1, T+1):
    words = list(input()) #CAAABBA

    stack_pop(words)



    print("#{} {}".format(tc,stack_pop(words)))

