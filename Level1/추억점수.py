def solution(name, yearning, photo):
    answer = [0] * len(photo)

    for i in range(len(name)):
        for j in range(len(photo)):
            if name[i] in photo[j]:
                answer[j] += yearning[i]

    return answer