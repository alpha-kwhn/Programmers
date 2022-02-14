from itertools import permutations

k = 80
dungeons = [[80,20],[50,40],[30,10]]

def solution(k, deongeons):
    lis = list(permutations(dungeons, len(dungeons)))
    #print(lis)

    able = []

    for i in range(len(lis)):
        tmp = k
        count = 0
        for m in range(len(lis[i])):
            if tmp >= lis[i][m][0]:
                tmp = tmp - lis[i][m][1]
                count += 1
            else:
                break
        able.append(count)
    return max(able)


print(solution(k, dungeons))