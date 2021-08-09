n = 7
lost = [1, 4, 5, 7]
reserve = [2, 3]


def solution(n, lost, reserve):
    list = [1] * n
    for i in reserve:
        list[i-1] = 2
    for i in lost:
        if i not in reserve:
            list[i-1] = 0
        else:
            list[i-1] = 1
    print(list)
    for i in range(len(list)):
        if i == 0:
            if list[i] == 0 and list[i+1] == 2:
                list[i] = 1
                list[i+1] = 1
        if i == (len(list) - 1):
            if list[i] == 0 and list[i-1] == 2:
                list[i] = 1
                list[i-1] = 1
        else:
            if list[i] == 0 and list[i-1] == 2:
                list[i] = 1
                list[i-1] = 1
            elif list[i] == 0 and list[i+1] == 2:
                list[i] = 1
                list[i+1] = 1
    print(list)
    return n - list.count(0)




did = solution(n, lost, reserve)
print(did)

