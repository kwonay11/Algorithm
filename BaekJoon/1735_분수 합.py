import math
def lcm(x, y):
    return x*y //math.gcd(x,y)
# A:분자 B:분모
A1, B1 = map(int,input().split())
A2, B2 = map(int,input().split())

g1 = math.gcd(A1, B1)
if g1 != 1:
    A1 //= g1
    B1 //= g1

g2 = math.gcd(A2, B2)
if g2 != 1:
    A2 //= g2
    B2 = B2 // g2


#B의 최소공배수를 구하고
result_B = lcm(B1,B2)
#분자
result_A = (result_B//B1*A1) + (result_B//B2*A2)


print(result_A, result_B)
