arr = [4,3,2,1]

def solution(arr):
    answer = []
    small = min(arr)
    arr.remove(small)
    if len(arr) == 0:
        answer.append(-1)
        return answer
    else:
        return arr

did = solution(arr)
print(did)