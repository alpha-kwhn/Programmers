def solution(sequence, k):
    answer = []
    count = 0
    start = 0

    for i in range(len(sequence)):
        count += sequence[i]

        if count > k:
            while count > k:
                count -= sequence[start]
                start += 1

        if count == k:
            answer.append([(i - start) + 1, start, i])

    answer.sort(key=lambda x: x[0])
    return answer[0][1:]