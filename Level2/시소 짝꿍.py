from collections import Counter

# 2,3,4
def solution(weights):
    # 0. 시소 짝꿍 개수 집계하는 변수
    answer = 0
    ratio = [3/2, 2/3, 4/2, 2/4, 4/3, 3/4]
    # 1. 특정 무게를 기준으로 해당 무게를 가진 사람이 몇명인지 집계
    counter = Counter(weights)
    # 2. weights 리스트에 중복요소 제거
    weights = list(set(weights))
    # 3. 시소 짝꿍 집계
    while weights:
        # 3.1 짝꿍 찾는 대상 값을 맨앞에서 취득 후 리스트 상에서 삭제
        target = weights.pop(0)
        # 3.2 자신과 같은 무게인 사람들이 여럿일때 형성되는 짝꿍의 수 집계
        if counter[target] > 1:
            answer += ((counter[target] * (counter[target] - 1)) // 2)
        # 3.3 짝꿍의 존재 확인
        for j in ratio:
            # 3.3.1 target과 짝꿍이 될 수 있는 비율의 값이 정수 형태일 경우
            if target * j == float(int(target * j)):
                # 3.3.2 해당 값이 weights에 존재하는 경우
                if int(target * j) in weights:
                    # 3.3.3 target과 같은 무게인 사람수만큼 짝꿍의 개수 추가
                    answer += (counter[target] * counter[int(target * j)])
    return answer