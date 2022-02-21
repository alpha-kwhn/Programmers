s = "}}}"

def solution(s):
    num = 0
    for i in range(len(s)):
        a = s[:i]
        b = s[i:]
        tmp = b + a
        lis = []
        flag = 1

        for k in range(0, len(tmp)):
            if tmp[k] == '}' and len(lis) == 0:
                flag = 0
                break
            elif tmp[k] == '}' and len(lis) != 0:
                if lis[-1] == '{':
                    if len(lis) == 1:
                        lis.clear()
                    else:
                        lis = lis[:-1]
                elif tmp[k] == '}' and lis[-1] != '{':
                    flag = 0
                    break
            elif tmp[k] == '{':
                lis.append(tmp[k])

            if tmp[k] == ']' and len(lis) == 0:
                flag = 0
                break
            elif tmp[k] == ']' and len(lis) != 0:
                if lis[-1] == '[':
                    if len(lis) == 1:
                        lis.clear()
                    else:
                        lis = lis[:-1]
                elif tmp[k] == ']' and lis[-1] != '[':
                    flag = 0
                    break
            elif tmp[k] == '[':
                lis.append(tmp[k])

            if tmp[k] == ')' and len(lis) == 0:
                flag = 0
                break
            elif tmp[k] == ')' and len(lis) != 0:
                if lis[-1] == '(':
                    if len(lis) == 1:
                        lis.clear()
                    else:
                        lis = lis[:-1]
                elif tmp[k] == ')' and lis[-1] != '(':
                    flag = 0
                    break
            elif tmp[k] == '(':
                lis.append(tmp[k])

        if len(lis) != 0:
            flag = 0

        if flag == 1:
            num += 1
    return num

print(solution(s))







