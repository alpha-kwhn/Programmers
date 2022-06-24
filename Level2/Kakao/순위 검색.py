info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]


def check(dict, dict_info):
    if dict == "-":
        return True
    else:
        if dict == dict_info:
            return True
        else:
            return False


def solution(info, query):
    answer = [0]*len(query)
    num = 0
    qu = [0, 2, 4, 6, 7]
    inf = [0, 1, 2, 3, 4]
    for i in query:
        refactor_ = i.split()
        refactor_[7] = int(refactor_[7])
        for j in info:
            refactor = j.split()
            refactor[4] = int(refactor[4])
            flag = 1
            for p in range(4):
                if check(refactor_[qu[p]], refactor[inf[p]]):
                    continue
                else:
                    flag = 0
                    break
            if refactor_[7] > refactor[4]:
                flag = 0
            if flag == 1:
                answer[num] += 1
        num += 1
    return answer


print(solution(info, query))

