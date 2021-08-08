answers = [1, 3, 2, 4, 2]
counts = [0, 0, 0]
def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    length = len(answers) #리스트의 길이
    a_point = 0
    b_point = 0
    c_point = 0

    for i in range(length):
        if a[i%5] == answers[i]:
            counts[0] += 1
            a_point += 1

    for i in range(length):
        if b[i%8] == answers[i]:
            counts[1] += 1
            b_point += 1

    for i in range(length):
        if c[i%10] == answers[i]:
            counts[2] += 1
            c_point += 1

    winner = []
    for i in range(3):
        if counts[i] == max(counts):
            winner.append(i)






    liste = [a_point, b_point, c_point]
    answer = []

    if a_point == b_point and a_point == c_point and b_point == c_point:
        answer = [1, 2, 3]
    elif a_point == b_point and a_point > c_point:
        answer = [1, 2]
    elif a_point == c_point and a_point > b_point:
        answer = [1, 3]
    elif c_point == b_point and b_point > a_point:
        answer = [2, 3]
    elif a_point > b_point and a_point > c_point:
        answer = [1]
    elif b_point > a_point and b_point > c_point:
        answer = [2]
    elif c_point > b_point and c_point > a_point:
        answer = [3]

    return answer

did = solution(answers)
print(did)





