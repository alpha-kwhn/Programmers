s = "a B z"
n = 4

def solution(s, n):
    alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"
           , "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    alp2 = []
    answer = ""
    for i in range(len(alp)):
        target = alp[i].upper()
        alp2.append(target)

    for i in s:
        if i != "" and i.islower():
            index = (alp.index(i) + n) % len(alp) #26
            answer += alp[index]
        elif i != "" and i.isupper():
            index = (alp2.index(i) + n) % len(alp2)  # 26
            answer += alp2[index]
        else:
            answer += " "
    return answer


did = solution(s, n)
print(did)
