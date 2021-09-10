import re

s = "{{123}}"

def solution(s):
    tmp = re.split(r'^{(\d),$', s[1:-1])
    ans = tmp[0]
    res = ans.replace('{', '')
    res = res.split('},')
    res[-1] = res[-1].replace('}', '')

    answer = []
    for i in res:
        lis = []
        st = ''
        for j in i:
            if j != ',':
                st += j
            else:
                lis.append(st)
                st = ''
        lis.append(st)
        answer.append(lis)
    answer.sort(key = len)

    final = []
    for i in answer:
        for j in i:
            if j not in final:
                final.append(j)
    final = list(map(int, final))
    return final


did = solution(s)
print(did)