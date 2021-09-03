progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

def solution(progresses, speeds):
    time = 1
    answer = []
    while max(progresses) != 0:
        for i in range(len(progresses)):
            progresses[i] += (time * speeds[i])
        count = 0
        for i in range(len(progresses)):
            if progresses[i] >= 100:
                progresses[i] = 0
                speeds[i] = 0
                count += 1
                if i == len(progresses) - 1:
                    answer.append(count)
            elif progresses[i] > 0 and progresses[i] < 100:
                if count > 0:
                    answer.append(count)
                break
    return answer



did = solution(progresses, speeds)
print(did)