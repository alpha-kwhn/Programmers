# 2이상 100이하의 수 중 하나를 골라, 해당 수보다 작거나 같은 카드들, 상자들 준비
# 상자에 카드를 하나씩 넣음 -> 상자를 섞음 -> 일렬로 나열 -> 순서에 따라 1번부터 번호부여
# 임의의 상자 하나를 선택 -> 선택한 상자 안의 숫자 카드 확인 -> 카드에 적힌 번호의 상자 -> 카드 확인
# 위 과정 계속 반복 -> 열어야 하는 상자가 이미 열려있는 경우가 올때까지
# 1번 그룹 제외하고 남는 상자가 없다면 게임 종료 + 0점
# 있다면 동일과정 반복 -> 2번 상자 그룹
# 게임점수는 1번 상자 그룹에 속한 상자 수 x 2번 상자 그룹에 속한 상자 수
def solution(cards):
    result = []

    for i in range(len(cards)):
        start = i + 1
        opened = [False] * len(cards)
        checked = 0
        answer = 0

        while opened[start - 1] == False:
            opened[start - 1] = True
            start = cards[start - 1]
            checked += 1

        if checked == len(cards):
            result.append(0)
            continue

        else:
            answer = checked
            checked = 0

        for j in range(len(cards)):
            if opened[j] == True:
                continue
            else:
                start = j + 1
                while opened[start - 1] == False:
                    opened[start - 1] = True
                    start = cards[start - 1]
                    checked += 1
                result.append(answer * checked)
                checked = 0

    return max(result)