from collections import OrderedDict


def solution(keymap, targets):
    answer = []
    diction = {}
    # 1. target에 있는 문자열을 완성하기 위해 필요한 알파벳 조사 & 알파벳 순서에 맞게 알파벳 정렬
    tmp = ''.join(targets)
    tmp = ''.join(OrderedDict.fromkeys(tmp))

    # 2. keymap 문자열 탐색하며 가장 적은 횟수로 알파벳 쓸 수 있는 경우 찾기
    for i in tmp:
        for j in keymap:
            # 3. target 문자열에 들어가는 문자가 keymap에서 몇번째 index에 있는지 확인
            index = j.find(i)
            # 3.1 targets에 속한 알파벳의 딕셔너리 값이 존재한다면
            if i in diction:
                # 3.1.1 만일 딕셔너리 값이 0이라면 continue
                if diction[i] == 0:
                    continue
                # 3.1.2 딕셔너리 값이 0이 아니라면
                else:
                    # 3.2.1 딕셔너리 값이 -1이 아니고, keymap에서 찾을 수 있는 알파벳이면서 기존 딕셔너리 값보다 index가 작은경우
                    if diction[i] != -1 and diction[i] > index and index != -1:
                        # 값 교체
                        diction[i] = index
                    # 3.2.2 딕셔너리 값이 -1인데 index 값이 -1이 아닌경우
                    elif diction[i] == -1 and index != -1:
                        # 값 교체
                        diction[i] = index
                    # 3.2.3 keymap에서 target을 구성하는 알파벳을 찾을 수 없는 경우 -> continue
                    elif index == -1:
                        continue
            # 3.3 target에 속한 알파벳의 딕셔너리 값이 없다면, keymap에서 찾은 알파벳의 index 값을 대입
            else:
                diction[i] = index
    # 4. 정답 내기
    for i in targets:
        count = 0
        # 4.1 target의 영단어 속 알파벳을 키로 가지는 딕셔너리의 value가 -1이 아니라면 count에 (diction[j] + 1)을 추가
        # -1이라면 배열에 -1을 넣어주고 break해서 값이 훼손되는 것을 방지
        for j in i:
            if diction[j] != -1:
                count += (diction[j] + 1)
            else:
                count = -1
                break
        answer.append(count)

    return answer