s = "pPoooyY"

def solution(s):
    c1 = s.count("p")
    c2 = s.count("P")
    c3 = s.count("y")
    c4 = s.count("Y")

    if c1+c2 == c3+c4:
        return True
    else:
        return False


did = solution(s)
print(did)