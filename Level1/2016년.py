a = 5
b = 24


def solution(a, b):
    month = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    if a == 1:
        target = b % 7
    else:
        target = (month[a-2] + b) % 7

    answer = days[target-1]
    return answer


did = solution(a, b)
print(did)