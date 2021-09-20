arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]

def solution(arr):
    answer = []
    for i in range(0, len(arr), 2):
        total = []
        lis = []
        for q in range(i, i+2):
            for j in range(i, i+2):
                lis.append(arr[q][j])
            if lis.count(1) == 0:
                total.append([0])
            elif lis.count(0) == 0:
                total.append([1])
            else:
                total.append(lis)

        flag = 0
        for o in range(1, len(total)):
            if total[0] != total[o]:
                flag = 1
                break
        if flag == 1:
            answer.append(total)
        else:
            answer.append(total[0])
    return answer


did = solution(arr)
print(did)



