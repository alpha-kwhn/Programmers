s = "3people unFollowed me"

def solution(s):
    lis = s.split(' ')
    answer = []
    answer2 = ''
    for i in lis:
        answer.append(i.capitalize())
    for i in range(len(answer)):
        answer2 += answer[i]
        if i != len(answer) - 1:
            answer2 += ' '
    return answer2

did = solution(s)
print(did)