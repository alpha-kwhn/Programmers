from collections import deque

# 현 좌표가 타당한 좌표값인지 판별해주는 함수
def isOk(x, y, width, height):
    return x >= 0 and x < height and y >= 0 and y < width

def solution(maps):
    # 현재 map의 너비와 높이
    width = len(maps[0])
    height = len(maps)

    # 방문 여부를 체크하는 배열 --> 미방문 0, 방문 1
    index = [[0] * len(maps[0]) for i in range(len(maps))]

    # BFS에서 활용할 Queue --> 초기 값에는 캐릭터의 시작위치 좌표를 넣어준다
    queue = deque([[[0, 0]]])

    # x, y축 방향의 direction들
    dir_x = [-1, 1, 0, 0]
    dir_y = [0, 0, -1, 1]

    # 이동거리를 집계하는 변수
    answer = 0

    while queue:
        # 1. 인접 좌표를 모두 저장하는 임시 배열
        container = []

        # 2. 큐의 맨 앞에 있는 원소를 pop
        tmp = queue.popleft()

        # 3. 인접 노드들 for문으로 모두 방문하며 BFS 실행
        for i in tmp:

            # 4.1 만일 현재 좌표가 목적지라면 BFS 탐색을 마무리한다
            if i[0] == (height - 1) and i[1] == (width - 1):
                answer += 1
                return answer

            # 4.2 만일 현재 좌표가 목적지가 아니라면 BFS 이어서 진행
            else:
                # 5.1 현재 좌표에 인접한 상하좌우 좌표 값들이 타당한 값이면서 방문했던 곳인지 검사
                # 5.2 그 다음엔 해당 좌표값이 벽인지 공간인지를 검사

                # 우
                if isOk(i[0] + dir_x[3], i[1] + dir_y[3], width, height) and index[i[0] + dir_x[3]][
                    i[1] + dir_y[3]] == 0 and maps[i[0] + dir_x[3]][i[1] + dir_y[3]] == 1:
                    # 6. 인접 좌표값 담는 배열에 좌표 추가 & 해당 좌표 방문처리 해주기 (효율성 향상)
                    container.append([i[0] + dir_x[3], i[1] + dir_y[3]])
                    index[i[0] + dir_x[3]][i[1] + dir_y[3]] = 1

                # 하
                if isOk(i[0] + dir_x[1], i[1] + dir_y[1], width, height) and index[i[0] + dir_x[1]][
                    i[1] + dir_y[1]] == 0 and maps[i[0] + dir_x[1]][i[1] + dir_y[1]] == 1:
                    container.append([i[0] + dir_x[1], i[1] + dir_y[1]])
                    index[i[0] + dir_x[1]][i[1] + dir_y[1]] = 1

                # 상
                if isOk(i[0] + dir_x[0], i[1] + dir_y[0], width, height) and index[i[0] + dir_x[0]][
                    i[1] + dir_y[0]] == 0 and maps[i[0] + dir_x[0]][i[1] + dir_y[0]] == 1:
                    container.append([i[0] + dir_x[0], i[1] + dir_y[0]])
                    index[i[0] + dir_x[0]][i[1] + dir_y[0]] = 1

                # 좌
                if isOk(i[0] + dir_x[2], i[1] + dir_y[2], width, height) and index[i[0] + dir_x[2]][
                    i[1] + dir_y[2]] == 0 and maps[i[0] + dir_x[2]][i[1] + dir_y[2]] == 1:
                    container.append([i[0] + dir_x[2], i[1] + dir_y[2]])
                    index[i[0] + dir_x[2]][i[1] + dir_y[2]] = 1

        # 7. 더 이상 갈 곳이 없으면 -1 return
        if len(container) == 0:
            return -1

        # 8. 인접 노드 탐색이 끝나면 이동거리 +1 해준다
        answer += 1

        # 9. 인접 노드들을 모두 담은 배열을 queue에 넣어준다
        queue.append(container)