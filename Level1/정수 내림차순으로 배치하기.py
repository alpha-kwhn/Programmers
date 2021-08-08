n = 118372

def solution(n):
    tmp = str(n)
    lis = []
    answer = ""
    for i in range(len(tmp)):
        lis.append(tmp[i])
    lis = list(map(int, lis))
    lis.sort()
    lis.reverse()
    lis = list(map(str,lis))
    for i in lis:
        answer += i
    answer = int(answer)
    return answer

did = solution(n)
print(did)