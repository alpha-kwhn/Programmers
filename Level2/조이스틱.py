name = "JEROEN"
name1 = "JAN"
name2 = "ABAAAAAAAAABB"
name3 = "BBBAAB"

def solution(name):
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S'
        , 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    lis = [0] * len(name)
    for i in range(len(name)):
        if name[i] != 'A':
            if alpha.index(name[i]) > len(alpha) - alpha.index(name[i]):
                lis[i] = len(alpha) - alpha.index(name[i])
            else:
                lis[i] = alpha.index(name[i])
    start = 0
    move = sum(lis)
    lis[0] = 0
    while sum(lis) != 0:
        if start + 1 == len(lis):
            start = -1
        if lis[start + 1] != 0 and lis[start - 1] != 0:
            start += 1
            move += 1
            lis[start] = 0
        elif lis[start + 1] != 0 and lis[start - 1] == 0:
            start += 1
            move += 1
            lis[start] = 0
        elif lis[start + 1] == 0 and lis[start - 1] != 0:
            start -= 1
            move += 1
            lis[start] = 0
        else:
            sle = 2
            while True:
                tmp = start + sle
                tmp2 = start - sle
                if abs(tmp2) + tmp == len(lis):
                    start = tmp2
                    move += sle
                    lis[tmp2] = 0
                    break
                if lis[tmp] != 0 and lis[tmp2] == 0:
                    start += sle
                    move += sle
                    lis[start] = 0
                    break
                elif lis[tmp] == 0 and lis[tmp2] != 0:
                    start -= sle
                    move += sle
                    lis[start] = 0
                    break
                else:
                    sle += 1
    return move

did3 = solution(name3)
print(did3)
