def solution(s):
    answer = 0
    target = []
    same = 0
    diff = 0

    for i in range(0, len(s)):
        if len(target) == 0:
            target.append(s[i])
            same += 1
        else:
            if s[i] == target[0]:
                same += 1
            else:
                diff += 1

        if same == diff:
            answer += 1
            target = []

    if len(target) != 0:
        answer += 1

    return answer