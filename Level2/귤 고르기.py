from collections import Counter
import operator


def solution(k, tangerine):
    answer = 0
    sell = k

    # 1. 귤 크기 배열 딕셔너리로 만들어줌
    diction = Counter(tangerine)

    # 2. 딕셔너리 내림차순 정렬
    dics = sorted(diction.items(), key=operator.itemgetter(1), reverse=True)

    # 3. 정답구하기
    for j in dics:
        sell -= j[1]
        if sell <= 0:
            return answer + 1
        else:
            answer += 1