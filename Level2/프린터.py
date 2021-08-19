from collections import deque

priorities = [1, 1, 9, 1, 1, 1]
location = 0


def solution(priorities, location):
    locate = []
    answer = []
    for i in range(len(priorities)):
        locate.append(i)

    pairs = dict(zip(locate, priorities))

    dq = deque(locate)
    while len(dq) != 0:
        tmp = dq.popleft()
        if pairs[tmp] < max(priorities):
            dq.append(tmp)
        elif pairs[tmp] == max(priorities):
            answer.append(tmp)
            priorities.remove(pairs[tmp])
        else:
            answer.append(tmp)
    return (answer.index(location)) + 1





did = solution(priorities, location)
print(did)










