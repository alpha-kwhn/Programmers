n = 5000

def solution(n):
    target = format(n, 'b')
    return target.count('1')
    #계속 2로 나눌때, 나머지가 0이 아니면, 점프가 필요하다
    #따라서 2진수로 바꾸고 1개수만 세면된다


did = solution(n)
print(did)