def solution(k, ranges):
    answer = []
    graph = [[0, k]]
    size = [0]
    count = 0

    # 콜라츠 추측
    while k > 1:
        count += 1
        if k % 2 == 1:
            k = (3 * k) + 1
            graph.append([count, k])
        else:
            k = k // 2
            graph.append([count, k])

        target = round(max(graph[count - 1][1], k), 1) - round((abs(k - graph[count - 1][1]) / 2), 1)
        size.append(target)

    # 넓이 구하기
    for item in ranges:
        cut_1 = item[0]
        cut_2 = count + item[1]

        if cut_1 > cut_2:
            answer.append(-1.0)
        elif cut_1 == cut_2:
            answer.append(0.0)
        else:
            target = sum(size[cut_1 + 1:cut_2 + 1])
            answer.append(target)

    return answer