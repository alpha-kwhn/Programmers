s = "try hello world"


def solution(s):
    answer = ""
    count = 0

    for i in range(0, len(s)):
        if s[i] != " ":
            if count % 2 != 0:
                answer += s[i].lower()
                count += 1
            elif count % 2 == 0:
                answer += s[i].upper()
                count += 1
        else:
            answer += " "
            count = 0

    return answer


did = solution(s)
print(did)
