def solution(players, callings):
    dict1 = {}
    dict2 = {}
    answer = []

    # 플레이어들의 인덱스 저장
    # mumu:0, soe:1, poe:2, kai:3, mine:4
    # 0: mumu, 1:soe, 2: poe, 3: kai, 4: mine
    for i in range(len(players)):
        dict1[players[i]] = i
        dict2[i] = players[i]

    # 교체
    for i in callings:
        # 3
        idx = dict1[i]
        # 2
        idx2 = dict1[i] - 1
        # poe
        target = dict2[idx2]
        # dict2[2] = kai
        # dict2[3] = poe
        dict2[idx2] = i
        dict2[idx] = target
        dict1[i] = idx2
        dict1[target] = idx

    # 정답출력
    for i in range(len(players)):
        answer.append(dict2[i])

    return answer