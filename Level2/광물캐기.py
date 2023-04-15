import copy

def solution(picks, minerals):
    dia = [1, 5, 25]
    irons = [1, 1, 5]
    stones = [1, 1, 1]
    trial = len(minerals) // 5
    flag = 0
    stress = []
    answer = 0
    cut = []

    for i in range(len(picks)):
        if i == 0:
            cut.append(picks[i])  # 0
        elif i == 1:
            cut.append(sum(picks[:2]))  # 1,2,3,
        elif i == 2:
            cut.append(sum(picks))  # 4, 5

    # 곡괭이질 횟수를 집계
    if len(minerals) % 5 == 0:
        flag = 0
    else:
        flag = 1

    # 다이아 피로도/ 철 피로도/ 돌 피로도/ 인덱스
    for i in range(trial):
        target = minerals[i * 5:5 * (i + 1)]
        tmp = [0, 0, 0, i]
        for j in target:
            if j == "diamond":
                tmp[0] += 1
                tmp[1] += 5
                tmp[2] += 25
            elif j == "iron":
                tmp[0] += 1
                tmp[1] += 1
                tmp[2] += 5
            else:
                tmp[0] += 1
                tmp[1] += 1
                tmp[2] += 1
        stress.append(tmp)

    # flag == 1인 경우 예외처리
    if flag == 1:
        target = minerals[5 * trial:]
        tmp = [0, 0, 0, trial]
        for j in target:
            if j == "diamond":
                tmp[0] += 1
                tmp[1] += 5
                tmp[2] += 25
            elif j == "iron":
                tmp[0] += 1
                tmp[1] += 1
                tmp[2] += 5
            else:
                tmp[0] += 1
                tmp[1] += 1
                tmp[2] += 1
        stress.append(tmp)

    locate = 0

    # 캘 수 없는 광물캐기 걸러내기
    able = stress[:cut[-1]]

    # able 리스트의 복사본 생성 + 피로도 기준 내림차순 정렬
    infos = copy.deepcopy(able)
    infos.sort(key=lambda x: -x[2])

    best = 0

    # 최소 피로도 계산
    for i in range(len(infos)):
        if picks[best] == 0:
            while picks[best] == 0:
                best += 1
                if best > 2:
                    return answer
        answer += infos[i][best]
        picks[best] -= 1

    return answer
