n = 78

def solution(n):
    k = 1
    nb = format(n, 'b')
    comp = str(nb)
    count = 0
    for i in range(len(comp)):
        if comp[i] == '1':
            count += 1

    while True:
        target = 0
        b = format(n + k, 'b')
        tmp = str(b)
        for i in range(len(tmp)):
            if tmp[i] == '1':
                target += 1
        if target == count:
            return n + k
        else:
            k += 1

did = solution(n)
print(did)