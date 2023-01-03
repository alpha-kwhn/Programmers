def solution(a, b):
    which_date = 0  # t의 값을 결정함

    how_many_days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 1월부터 12월

    for days in how_many_days_in_month:
        which_date = sum(
            how_many_days_in_month[0:a-1]) + b  # 1월부터 a월까지의 날 수 합 + b = 전체 일 수 / # sum 함수, listing 기본 다시 잡아야겠다... ㅠㅠ
    print(which_date)
    day_of_the_week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    answer = ""

    # 여기서부터 오류 발생...

    if a != 1:
        answer = which_date % 7
    else:
        answer = b % 7

    ans = day_of_the_week[answer - 1]
    return ans


a = 5
b = 24
day = solution(a, b)
print(day)  # 'TUE'