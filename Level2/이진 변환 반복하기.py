s = "110010101001"

def solution(s):
    count = 0
    num = 0
    while s != '1':
        num += s.count('0')
        s = s.replace('0', '')
        target = format(len(s), 'b')
        count += 1
        s = str(target)
    return [count, num]


did = solution(s)
print(did)