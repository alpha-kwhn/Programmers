from collections import deque

def solution(n, computers):
    # 네트워크의 개수를 집계하는 변수
    answer = 0

    # 탐색을 완료한 컴퓨터를 체크하는 리스트 -> 탐색완료시 1로 값을 변경
    index = [0] * len(computers)

    # 연속적인 컴퓨터를 지속해서 찾는 BFS 함수
    # 연속적인 컴퓨터를 발견한 현재 컴퓨터 인덱스 값을 활용
    def BFS(now):
        # 1. 현재 컴퓨터와 연결된 모든 컴퓨터 찾아내기

        # 1.1 연결된 컴퓨터 관계를 담을 임시 리스트
        tmp = []

        # 1.2 BFS 시작지점 컴퓨터 인덱스 찾기
        for i in range(len(computers)):
            # 1.2.1 시작 지점 찾으면 반복문 종료
            if len(tmp) != 0:
                break
            # 1.2.2 시작 지점 아직 찾는 중일 경우
            else:
                # 1.3.1 연결된 컴퓨터 찾았을 경우
                if computers[now][i] == 1 and now != i:
                    # 1.3.1.1 연결된 컴퓨터 관계 수집
                    tmp.append([now, i])
                    # 1.3.1.2 연결관계 0으로 변경
                    computers[now][i] = 0
                    computers[i][now] = 0
                    # 1.3.1.3 연결된 새 컴퓨터에 방문 했음을 표시
                    index[i] = 1
                # 1.3.2 연결된 컴퓨터를 못찾았으면 continue
                else:
                    continue

        # 1.3 연결된 컴퓨터 관계 수집이 끝나면 tmp를 바탕으로 queue 생성
        queue = deque([tmp])

        # 2. 인접한 컴퓨터가 없을때까지 계속 BFS 탐색을 진행

        # queue가 빌때까지 BFS 진행 -> queue가 빈다는 것은 곧 네트워크 하나가 온전히 형성되었음을 의미
        while queue:
            # 2.1 queue의 맨 앞에 있는 값 pop
            items = queue.popleft()

            # 2.2 tmp를 순회하며 새로 찾은 연결된 컴퓨터에서 또 연결된 컴퓨터가 있는지 탐색
            for i in items:
                # 2.2.1 연결된 컴퓨터 존재 시에
                if computers[i[1]].count(1) > 1:  # computers[1]
                    # 2.2.2 연결되어 있는 새로운 컴퓨터 모두 탐색
                    tmp = []
                    for k in range(len(computers)):
                        # 연결된 새로운 컴퓨터 발견시
                        if computers[i[1]][k] == 1 and i[1] != k:
                            # 2.2.3.1 연결된 새로운 컴퓨터 관계 수집
                            tmp.append([i[1], k])
                            # 2.2.3.2 새로 찾은 연결된 컴퓨터 방문여부 체크
                            index[k] = 1
                            # 2.2.3.3 컴퓨터 관계 0으로 만들어줌
                            computers[k][i[1]] = 0
                            computers[i[1]][k] = 0
                    # 2.2.3 연결된 컴퓨터 관계 수집이 끝나면 tmp를 queue에 넣어준다
                    queue.append(tmp)
                # 2.2.4 연결된 컴퓨터 없을 시에는 방문체크만 진행
                else:
                    # 방문여부 체크
                    continue

    # 모든 컴퓨터 네트워크 관계를 탐색한다
    for i in range(len(computers)):
        # 독립적 네트워크 발견 -> 개수 +1
        if computers[i].count(1) == 1:
            # 미방문 상태일 때
            if index[i] == 0:
                answer += 1
                # 방문확인 표시
                index[i] = 1
            # 이미 방문했을 경우
            else:
                continue
        # 연속적인 네트워크 발견
        else:
            # 현재 컴퓨터는 방문을 했음을 표시
            index[i] = 1
            BFS(i)  # 연속적인 네트워크를 발견한 현재 컴퓨터 인덱스 값을 넣어줌
            answer += 1

    return answer