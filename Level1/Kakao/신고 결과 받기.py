def solution(id_list, report, k):
    # 중복되는 신고는 동일하게 처리함 따라서 중복제거
    tmp = set(report)
    report = tmp

    # 딕셔너리 초기화
    penalty = {}
    blacklist = {}
    result = [0] * len(id_list)

    for i in id_list:
        penalty[i] = 0
        blacklist[i] = []

    # 신고 당한 횟수 집계 & 신고한 인물들 리스트 작성
    for i in report:
        lis = i.split()
        penalty[lis[1]] += 1
        blacklist[lis[0]].append(lis[1])

    # 메일 수신 횟수 집계
    for i in id_list:
        if penalty[i] >= k:
            for j in id_list:
                if i != j and i in blacklist[j]:
                    result[id_list.index(j)] += 1

    return result




