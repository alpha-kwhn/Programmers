strings = ["ae", "be", "ce", "ae"]
n = 1

def solution(strings, n):
    answer = []
    for i in range(len(strings)):
       strings[i] = strings[i][n]+strings[i]
    strings.sort()

    for i in range(len(strings)):
        strings[i] = strings[i][1:]
    answer = strings
    return answer

did = solution(strings, n)
print(did)