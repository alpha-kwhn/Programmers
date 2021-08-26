A = [1, 4, 2]
B = [5, 4, 4]

def solution(A, B):
    sum = 0
    A.sort()
    A.reverse()
    B.sort()
    for i in range(len(A)):
        for j in range(len(B)):
            target = A.pop() * B.pop()
            sum += target
    return sum

did = solution(A, B)
print(did)