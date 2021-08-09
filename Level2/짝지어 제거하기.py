s = "cdcd"

def solution(s):
    answer = ""
    answer += s[0]
    answer += s[1]
    if answer[0] == answer[1]:
        answer.clear()

    for i in range(2, len(s)-1):
        if s[i-1] != s[i] and s[i] != s[i+1]:
            answer += s[i]
        elif answer[-1] == s[i]:
            answer = answer[:-1]
    print(answer)

    if len(answer) == 0:
        return 1
    else:
        return 0

did = solution(s)
print(did)




