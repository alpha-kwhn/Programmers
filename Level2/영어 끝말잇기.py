n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
def solution(n ,words):
    lis = []
    answer = []
    for i in range(len(words)):
        if words[i] not in lis:
            lis.append(words[i])
            if len(lis) > 1:
                if lis[-1][0] != lis[-2][-1]:
                    answer.append((i % n) + 1)
                    answer.append((i // n) + 1)
                    return answer
        else:
            answer.append((i % n) + 1)
            answer.append((i // n) + 1)
            return answer
    return [0, 0]

did = solution(n, words)
print(did)