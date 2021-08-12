dartResult = "1D2S#10S"


def solution(dartResult):
    lis = []
    answer = []
    res = 0
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    num2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(len(dartResult)):
        lis.append(dartResult[i])

    for i in range(len(num)):
        for k in range(len(lis)):
            if num[i] == lis[k]:
                lis[k] = num2[i]
    print(lis)

    for i in range(len(lis)):
        if lis[i] == "S":
            tmp = answer.pop()
            answer.append(tmp)
        elif lis[i] == "D":
            tmp = answer.pop()
            answer.append(tmp * tmp)
        elif lis[i] == "T":
            tmp = answer.pop()
            answer.append(tmp * tmp * tmp)
        elif lis[i] == "*":
            tmp_a = answer.pop() * 2
            if len(answer) == 0:
                answer.append(tmp_a)
            else:
                tmp_b = answer.pop() * 2
                answer.append(tmp_b)
                answer.append(tmp_a)
        elif lis[i] == "#":
            tmp = answer.pop()
            answer.append(tmp * -1)
        elif lis[i] == 0 and lis[i-1] == 1:
            answer.pop()
            answer.append(10)
        else:
            answer.append(lis[i])

    return sum(answer)

did = solution(dartResult)
print(did)




