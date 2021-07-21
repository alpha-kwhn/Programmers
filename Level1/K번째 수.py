array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]

        con = array[i-1:j]
        con.sort()
        answer.append(con[k-1])
    return answer

kwk = solution(array, commands)
print(kwk)