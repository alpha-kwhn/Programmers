dirs = "ULURRDLLU"
dirs2 = "LRLRLRLLUUD"

def solution(dirs):
    x = 0
    y = 0
    answer = []
    for i in dirs:
        semi = []
        if i == 'L':
            if x > -5:
                tmp = [x, y]
                semi.append(tmp)
                x -= 1
                tll = [x, y]
                semi.append(tll)
                answer.append(semi)
        elif i == 'R':
            if x < 5:
                tmp = [x, y]
                semi.append(tmp)
                x += 1
                tll = [x, y]
                semi.append(tll)
                answer.append(semi)
        elif i == 'U':
            if y < 5:
                tmp = [x, y]
                semi.append(tmp)
                y += 1
                tll = [x, y]
                semi.append(tll)
                answer.append(semi)
        elif i == 'D':
            if y > -5:
                tmp = [x, y]
                semi.append(tmp)
                y -= 1
                tll = [x, y]
                semi.append(tll)
                answer.append(semi)
    new = []
    for i in answer:
        if i not in new:
            new.append(i)
    count = 0
    for i in new:
        nex = [i[1], i[0]]
        if nex in new:
            count += 1
    return len(new) - (count // 2)

did = solution(dirs)
print(did)
