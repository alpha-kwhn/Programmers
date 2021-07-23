arr = [1,1,3,3,0,1,1]


def solution(arr):
    list = ["00", "11", "22", "33", "44", "55", "66", "77", "88", "99"]
    list2 = ["0","1","2","3","4","5","6","7","8","9"]
    ans = []
    str1 = "".join(map(str, arr))

    for i in range(10):
        while list[i] in str1:
            str1 = str1.replace(list[i], list2[i])
        ans = str1

    answer = []
    for i in range(len(ans)):
        answer.append(ans[i])

    answer = [int(i) for i in answer]
    return answer


did = solution(arr)
print(did)