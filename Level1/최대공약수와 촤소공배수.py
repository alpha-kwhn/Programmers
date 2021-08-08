from math import gcd
from math import lcm

n = 3
m = 12

def solution(n, m):
    answer = []
    answer.append(gcd(n, m))
    answer.append(lcm(n, m))
    return answer

did = solution(n, m)
print(did)