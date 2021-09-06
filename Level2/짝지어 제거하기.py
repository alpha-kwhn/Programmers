s = "baabaa"

def solution(s):
    lis = []
    for i in s:
        lis.append(i)
        if len(lis) >= 2 and lis[-2] == lis[-1]:
            lis.pop()
            lis.pop()
    if len(lis) == 0:
        return 1
    else:
        return 0


did = solution(s)
print(did)

