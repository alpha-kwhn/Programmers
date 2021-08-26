s = "(())()"

def solution(s):
    arr1 = []
    if s[0] == ')':
        return False
    elif s[-1] == '(':
        return False
    else:
        for i in s:
            if i == '(':
                arr1.append(1)
            else:
                if len(arr1) == 0:
                    return False
                else:
                    arr1.pop()
        if len(arr1) == 0:
            return True
        else:
            return False


did = solution(s)
print(did)
