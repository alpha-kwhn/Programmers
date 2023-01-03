def solution(storey):
    # 층수의 절대값이 1 또는 10의 제곱수라면 return 1
    if abs(storey) == 1:
        return 1

    # 그 외의 경우
    else:
        # 2840
        answer = 0
        lengths = len(str(storey)) - 1  # 3
        firstNum = int(str(storey)[0])  # 2

        target1 = ((firstNum + 1) * (10 ** (lengths))) - storey  # 3000 - 2840 = 160
        tmp_lis = list(str(target1))  # ["1", "6", "0"]
        tmp1 = list(map(int, tmp_lis))  # [1, 6, 0]
        result1 = sum(tmp1)  # 7

        target2 = storey - (firstNum * (10 ** (lengths)))  # 2840 - 2000 = 840
        tmp_lis2 = list(str(target2))  # ["8", "4", "0"]
        tmp2 = list(map(int, list(str(target2))))  # [8, 4, 0]
        result2 = sum(tmp2)  # 12

        if target1 < target2:
            answer += result1

            if int(str(((firstNum + 1) * (10 ** (lengths))))[0]) <= 5:
                answer += int(str((firstNum + 1) * (10 ** (lengths)))[0])
            else:
                answer += (1 + (10 - int(str((firstNum + 1) * (10 ** (lengths)))[0])))

            return answer

        else:
            answer += result2

            if int(str(((firstNum) * (10 ** (lengths))))[0]) <= 5:
                answer += int(str(((firstNum) * (10 ** (lengths))))[0])
            else:
                answer += (1 + (10 - int(str(((firstNum) * (10 ** (lengths))))[0])))

            return answer


print(solution(88))
print(25 // 2)