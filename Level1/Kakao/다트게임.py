dartResult = "1D2S#10S"


def solution(dartResult):
    lis = []
    answer = []
    res = 0
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    num2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(len(dartResult)):
        lis.append(dartResult[i]) #리스트로 하나하나 옮기기

    for i in range(len(num)):
        for k in range(len(lis)):
            if num[i] == lis[k]:
                lis[k] = num2[i] #숫자인 얘들은 연산을 위해서 정수로 변환시키기

    for i in range(len(lis)): #각 케이스 별로 점수 산출방식 적용시켜 연산
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
        elif lis[i] == 0 and lis[i-1] == 1: #10점일 경우 예외처리
            answer.pop()
            answer.append(10)
        else:
            answer.append(lis[i])

    return sum(answer) #다 합하면 점수가 나옴

did = solution(dartResult)
print(did)




