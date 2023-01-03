def solution(s):
    answer = []

    for i in range(0, len(s)):
        if i == 0:
            answer.append(-1)
        else:
            if s[i] not in s[0:i]:
                answer.append(-1)
            else:
                index = s.find(s[i])
                lis = list(s)
                lis[index] = "0"
                s = ''.join(lis)
                answer.append(i - index)
    return answer
