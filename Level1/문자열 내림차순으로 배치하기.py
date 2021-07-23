s = "Zbcdefg"

def solution(s):
    lis = list(s)
    cik = []
    con = []
    for i in range(len(lis)):
        if lis[i].isupper() == True:
            con.append(lis[i])
    for i in lis:
        if i not in con:
            cik.append(i)

    con.sort(reverse=True)
    cik.sort(reverse=True)
    newer = cik + con
    answer = ''.join(newer)
    return answer

did = solution(s)
print(did)
