# 금액지불 -> 10일 간 회원자격
# 매일 1가지 제품 할인행사 진행, 할인상품은 하루에 하나씩만 구매 가능
def solution(want, number, discount):
    answer = 0
    for i in range(0, len(discount) - 9):
        flag = True
        target = discount[i:i + 10]
        for j in range(len(want)):
            if target.count(want[j]) == number[j]:
                continue
            else:
                flag = False
                break
        if flag:
            answer += 1

    return answer