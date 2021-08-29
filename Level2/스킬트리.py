skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]


def solution(skill, skill_trees):
    lis = []
    answer = ''
    anl = []
    correct = [0] * len(skill_trees)
    count = 0
    for i in range(len(skill)):
        lis.append(skill[i])
    for k in skill_trees:
        for i in range(len(k)):
            if k[i] in lis:
                answer += k[i]
        anl.append(answer)
        answer = ''

    for i in range(len(skill)):
        tmp = skill[:i+1]
        for j in range(len(anl)):
            if tmp == anl[j] and correct[j] != -1:
                count += 1
                correct[j] = -1
    for j in anl:
        pri = 0
        for k in range(len(j)):
            if j[k] in skill:
                pri += 1
        if pri == 0:
            count += 1
    return count



did = solution(skill, skill_trees)
print(did)
