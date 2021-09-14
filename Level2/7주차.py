enter = [1,4,2,3]
leave = [2,1,4,3]

def solution(enter, leave):
    stack = []
    count = [0] * len(enter)

    for i in enter:
        while True:
            if leave[0] in stack:
                stack.pop(stack.index(leave[0]))
                leave.pop(0)
            else:
                break
        stack.append(i)
        if len(stack) > 1:
            for p in stack:
                count[p-1] += 1
            count[i-1] = len(stack) - 1
    return count




did = solution(enter, leave)
print(did)