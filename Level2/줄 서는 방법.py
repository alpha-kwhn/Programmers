from itertools import permutations
import math


def solution(n, k):
    lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    target = lis[:n]
    answer = []

    for i in range(n):
        gap = math.factorial(n - (i + 1))
        answer.append(target[(k - 1) // gap])
        del target[(k - 1) // gap]
        print(answer)

    return answer
print(solution(3, 5))