s = "1 2 3 4"

def solution(s):
    lis = list(map(int, s.split()))
    return '%d %d' % (min(lis), max(lis)) #포맷팅 이용

did = solution(s)
print(did)