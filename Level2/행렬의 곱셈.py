arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]


def solution(arr1, arr2):
    ans = []
    lens = len(arr2[0])
    for i in range(len(arr1)):
        lis = []
        for j in range(lens):
            answer = 0
            for k in range(len(arr2)):
                answer += arr1[i][k] * arr2[k][j]
            lis.append(answer)
        ans.append(lis)
    return ans


did = solution(arr1, arr2)
print(did)
