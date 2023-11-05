def solution(n):
    answer = []

    def hanoi(n, start, sub, goal):
        if n == 1:
            answer.append([start, goal])
        else:
            # 1 -> 2 기둥으로 옮기기
            hanoi(n - 1, start, goal, sub)
            # 1 -> 3 기둥으로 맨 바닥 원판 옮기기
            answer.append([start, goal])
            # 2 -> 3 기둥으로 옮기기
            hanoi(n - 1, sub, start, goal)

    hanoi(n, 1, 2, 3)
    return answer