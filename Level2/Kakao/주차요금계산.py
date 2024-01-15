from datetime import datetime
from collections import defaultdict
import math


def solution(fees, records):
    dic = defaultdict(int)
    time_format = "%H:%M"
    time_history = defaultdict(int)
    state_history = defaultdict(str)
    answer = defaultdict(int)
    cash = []

    for item in records:
        check_time = datetime.strptime(item[:5], time_format)
        car_num = item[6:10]
        state = item[11:]

        if state == "IN":
            state_history[car_num] = state
            time_history[car_num] = check_time
        else:
            time_diff = int((check_time - time_history[car_num]).total_seconds() / 60)
            time_history[car_num] = 0
            state_history[car_num] = state
            dic[car_num] += time_diff

    for key, val in state_history.items():
        if val == "IN":
            deadline = datetime.strptime("23:59", time_format)
            time_diff = int((deadline - time_history[key]).total_seconds() / 60)
            dic[key] += time_diff

        if dic[key] > fees[0]:
            answer[key] = fees[1] + (math.ceil((dic[key] - fees[0]) / fees[2]) * fees[3])
        else:
            answer[key] = fees[1]

    target = dict(sorted(answer.items()))

    for val in target.values():
        cash.append(val)

    return cash
