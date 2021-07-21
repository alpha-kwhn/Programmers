lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

def solution(lottos, win_nums):
    zero_count = 0
    con = []
    answer = []
    for i in lottos:
        for j in win_nums:
            if i == j:
                con.append(i)

    for i in lottos:
        if i == 0:
            zero_count += 1

    max = len(con) + zero_count
    min = len(con)
    list = [max, min]

    for i in list:
        if i == 6:
            answer.append(1)
        elif i == 5:
            answer.append(2)
        elif i == 4:
            answer.append(3)
        elif i == 3:
            answer.append(4)
        elif i == 2:
            answer.append(5)
        else:
            answer.append(6)

    return answer


did = solution(lottos, win_nums)
print(did)