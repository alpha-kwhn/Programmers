def solution(food):
    answer = ''

    for i in range(1, len(food)):
        num = food[i] // 2
        answer += (str(i) * num)
    tmp = answer + '0'
    tmp += (answer[::-1])

    return tmp