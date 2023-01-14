# 점수가 K번째 이내이면 면전

def solution(k, score):
    answer = []
    tmp = []
    minimum = 0

    for i in range(0, len(score)):
        if len(answer) <= k - 1:
            tmp.append(score[i])
            answer.append(min(tmp))
        else:
            tmp.append(score[i])
            tmp.sort(reverse=True)
            answer.append(tmp[k - 1])

    return answer