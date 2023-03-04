def solution(cards1, cards2, goal):
    for i in goal:
        # 1. cards1, cards2의 리스트가 비지 않았을 때
        if len(cards1) > 0 and len(cards2) > 0:
            # 1.1 cards1의 맨 앞 단어가 i랑 다를 때
            if cards1[0] != i:
                # 1.1.1 cards2의 맨 앞 단어가 i랑 같을때
                if cards2[0] == i:
                    del cards2[0]
                # 1.1.2 cards2의 맨 앞 단어도 i랑 다를때
                else:
                    return "No"
            else:
                del cards1[0]
        # 2. cards1의 리스트는 비지 않았으나, cards2의 리스트는 비어있을 때
        elif len(cards1) > 0 and len(cards2) <= 0:
            # 2.1 cards1의 맨 앞 단어가 i랑 다를 때
            if cards1[0] != i:
                return "No"
            else:
                del cards1[0]

        # 3. cards1의 리스트는 비었으나, cards2의 리스트는 비지 않았을때
        elif len(cards1) <= 0 and len(cards2) > 0:
            # 3.1 cards2의 맨 앞 단어가 i랑 다를 때
            if cards2[0] != i:
                return "No"
            else:
                del cards2[0]

        # 4. 쓸 카드 없을때
        else:
            return "No"

    # 5. 정상적으로 리스트 순회가 끝나서 goal 단어로 문장 완성시
    return "Yes"