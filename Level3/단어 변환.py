from collections import deque

# a 문자열이 b로 변환이 가능한지를 판별하는 함수
def same(a, b, lenght):
    leng = 0

    for k in range(lenght):
        if a[k] == b[k]:
            leng += 1

    # 현재 문자에서 변환이 가능한 문자인 경우
    if leng == lenght - 1:
        return 1
    # 현재 문자에서 변환이 불가능한 문자인 경우
    else:
        return 0


def solution(begin, target, words):
    # 0. 문자열 변환 횟수를 담는 변수, words의 길이, begin 길이 값
    answer = 0
    words_len = len(words)
    lengths = len(begin)

    # 1. 방문여부 체크 리스트
    index = [0] * words_len

    # 2.1 target이 words에 없는 경우 -> 애초에 답찾기 불가능
    if target not in words:
        return 0

    # 2.2 target이 words에 있는 경우
    else:
        # 3.1 begin -> target으로 바로 변환이 가능한지 확인
        if same(begin, target, lengths) == 1:
            return 1
        # 3.2 begin -> target으로 바로 변환이 불가능한 경우 (몇 번 변환 거쳐야 함)
        else:
            # 4. 초기 queue에 들어갈 단어들 모으는 임시리스트
            tmp = []

            # 5. BFS 시작하기 전 queue에 넣을 초기값 수집
            for i in range(len(words)):
                # 6. 한글자 바꿔서 변환이 가능한경우 -> 임시 리스트에 추가
                if same(begin, words[i], lengths) == 1:
                    tmp.append(words[i])
                    # 변환 사용 여부 체크
                    index[i] = 1

            # 7.1 begin에서 변환가능한 단어가 있을 경우
            if len(tmp) > 0:
                # 8. 임시 리스트를 queue에 넣어서 queue가 빌 때까지 BFS 진행
                queue = deque([tmp])
                answer += 1
            else:
                # 7.2
                # target이 words에 있기는 하지만
                # 그 단어가 되기 위해 변환 과정을 거칠 단어가 없을 경우
                return 0

            # 9. BFS
            while queue:
                # 10. 같은 단계에서 찾은 변환 가능 문자가 있을시 담는 임시 리스트
                tmps = []
                # 11. popleft
                items = queue.popleft()

                # 12. 더 변환이 가능한 문자있는지 BFS
                for i in range(len(items)):
                    # 13.1 i가 target으로 바로 변환가능한가
                    if same(items[i], target, lengths) == 1:
                        return answer + 1

                    # 13.2 i가 target으로 바로 변환 불가능 -> 중간변환 문자열 찾아야함
                    else:
                        for j in range(words_len):
                            # 14. 변환 가능할 시
                            if items[i] != words[j] and same(items[i], words[j], lengths) == 1:
                                # 변환에서 안쓰인 문자열이라면
                                if index[j] == 0:
                                    # 15. tmp에 추가
                                    tmps.append(words[j])
                                    index[j] = 1

                # 16. tmp를 queue에 넣어줌
                queue.append(tmps)
                # 17. 변환횟수 증가
                answer += 1

            return answer
