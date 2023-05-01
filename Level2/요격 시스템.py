def solution(targets):
    
    # 시작 x좌표 기준으로 오름차순 정렬하기
    targets.sort(key=lambda x: (x[0], x[1]))
    lis = [[targets[0][0] + 0.1, targets[0][1] - 0.1]]

    # 개수 집계
    for i in range(1, len(targets)):

        # lis 맨 뒤의 구간과 겹치는 구간이 있을 경우
        first = lis[-1][0]
        second = lis[-1][1]
        t_first = targets[i][0] + 0.1
        t_second = targets[i][1] - 0.1

        if first <= t_first <= second:
            if t_second <= second:
                lis[-1][0] = t_first
                lis[-1][1] = t_second
            elif t_second > second:
                lis[-1][0] = t_first

        elif t_first < first:
            if t_second <= second:
                lis[-1][1] = t_second

        elif t_first > first:
            lis.append([t_first, t_second])

    return len(lis)