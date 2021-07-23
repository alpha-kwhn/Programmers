s = "a234"

def solution(s):
    if len(s) == 4 and s.isdigit() == True:
        return True
    elif len(s) == 6 and s.isdigit() == True:
        return True
    else:
        return False

did = solution(s)
print(did)