s1 = "abcde"
s2 = "qwer"


def solution(s):
    answer = ""
    if len(s) % 2 == 0:
        answer = s[(len(s)//2) - 1] + s[len(s)//2]
    else:
        answer = s[len(s)//2]
    return answer


did = solution(s1)
print(did)
did2 = solution(s2)
print(did2)