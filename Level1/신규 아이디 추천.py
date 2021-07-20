new_id = "z-+.^."


def solution(new_id):
    # 1
    new_id = new_id.lower()

    # 2
    answer = ''
    for i in new_id:
        if i.isalnum() or i in '-_.':
            answer += i

    # 3
    while '..' in answer:
        answer = answer.replace('..','.')

    # 4
    data = list(answer)

    if data[0] == '.':
        del data[0]

    elif data[-1] == '.':
        del data[-1]

    answer = "".join(data)
    #print(answer)


    # 5
    if answer == "":
        answer = "a"

    # 6
    first = []

    if len(answer) >= 16:
        answer = answer[0:15]

    if answer[-1] == ".":
        answer = answer[0:-1]

    # print(new_id)

    # 7
    first = []
    tmp = 'a'

    if len(answer) <= 3:
        answer = answer + answer[-1] * (3 - len(answer))

    return answer

did = solution(new_id)
print(did)

