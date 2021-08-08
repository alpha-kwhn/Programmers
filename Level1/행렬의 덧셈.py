arr1 = [[1],[2]]
arr2 = [[3],[4]]


def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        lis1 = []
        for j in range(len(arr1[0])):
            lis1.append(arr1[i][j]+arr2[i][j])
        answer.append(lis1)
    return answer


did = solution(arr1, arr2)
print(did)
