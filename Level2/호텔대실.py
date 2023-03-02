def plusTen(clock):
    hour = int(clock[:2])
    minute = int(clock[-2:]) + 10
    new_clock = 0

    # 10분 더했을 때 시각이 넘어가는 경우 -> 60분 차감 + 시각 1시간 증가
    if minute >= 60:
        minute -= 60
        hour += 1

        if hour < 10:
            hour = "0" + str(hour)
        else:
            hour = str(hour)

        if minute < 10:
            minute = "0" + str(minute)
        else:
            minute = str(minute)

        new_clock = int(hour + minute)
    else:
        if hour < 10:
            hour = "0" + str(hour)
        else:
            hour = str(hour)
        new_clock = int(hour + str(minute))

    print(new_clock)
    return new_clock


def solution(book_time):
    room = 0
    mini = []

    # 0. 배열에서 : 제거 + int로 형변환
    for i in book_time:
        i[0] = i[0].replace(':', '')
        i[1] = i[1].replace(':', '')

    # 1. 입실 시간을 기준으로 리스트 정렬하기
    book_time.sort(key=lambda x: x[0])

    # 2. 시간의 흐름에 따라 객실 배치하기
    for i in range(len(book_time)):
        # 3.1 객실이 전부 빈방일때
        if i == 0:
            mini.append(plusTen(book_time[i][1]))
            room += 1
        # 3.2 객실이 최소 하나라도 차있을 때
        else:
            # 3.2.3 청소가 끝나고의 시간을 바탕으로 객실 추가여부 판단
            if mini[0] <= int(book_time[i][0]):
                del mini[0]
            else:
                room += 1

            mini.append(plusTen(book_time[i][1]))
            mini.sort()

    return room