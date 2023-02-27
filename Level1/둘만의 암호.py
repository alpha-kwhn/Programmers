def solution(s, skip, index):
    # 정답 문자열
    answer = ""

    # 알파벳 리스트
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    # 비고려 알파벳 리스트에서 모두 제거
    for i in skip:
        alphabet.remove(i)

    # 문자열 변환 진행
    for j in s:
        tmp = (alphabet.index(j) + index) % len(alphabet)
        answer += alphabet[tmp]

    return answer