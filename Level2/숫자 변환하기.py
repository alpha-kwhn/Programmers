from collections import deque


def solution(x, y, n):
    answer = 0
    queue = deque([[x]])

    if x == y:
        return 0
    else:
        while queue:
            container = []
            tmp = queue.popleft()
            for i in tmp:
                if i * 2 == y or i * 3 == y or i + n == y:
                    return answer + 1
                else:
                    if i * 2 > y:
                        if i + n > y:
                            return -1
                        else:
                            container.append(i + n)
                    elif i * 2 < y and i * 3 > y:
                        if i + n > y:
                            container.append(i * 2)
                        else:
                            container.append(i * 2)
                            container.append(i + n)
                    elif i * 3 < y:
                        if i + n > y:
                            container.append(i * 2)
                            container.append(i * 3)
                        else:
                            container.append(i * 2)
                            container.append(i * 3)
                            container.append(i + n)
            if len(container) == 0:
                return -1
            else:
                container = list(set(container))
                queue.append(container)
                answer += 1
        return -1