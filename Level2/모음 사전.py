from itertools import product
word = "I"

def solution(word):
    lis = ['A', 'E', 'I', 'O', 'U']
    answer = []
    for i in range(1, 6):
        npr = list(map(''.join, product(lis, repeat = i)))
        answer += npr
    answer.sort()
    ans = answer.index(word)
    return ans + 1


did = solution(word)
print(did)