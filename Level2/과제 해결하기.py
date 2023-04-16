# 새 과제 시작시간 -> 기존 것 멈추고 새로운 과제를 시작
# 진행중인 과제 끝 -> 멈춰둔 과제 이어서 진행 (새로 시작하는 것이 있다면 그것이 우선으로 진행됨)
import copy


def solution(plans):
    answer = []
    waits = []

    # 시간에서 콜론제거하기
    for i in range(len(plans)):
        plans[i][1] = plans[i][1][:2] + plans[i][1][3:]

    # 시작시간을 기준으로 오름차순 정렬
    plans.sort(key=lambda x: x[1])

    # 알고리즘 실행
    for i in range(len(plans)):
        # 맨 끝 아닌경우 -> 바로 다음 타임과 비교를 해주어야 함
        if i < len(plans) - 1:
            hour = int(plans[i + 1][1][:2]) - int(plans[i][1][:2])
            minutes = int(plans[i + 1][1][2:]) - int(plans[i][1][2:])
            diff = (60 * hour) + minutes

            # 작업의 끝이 다음 작업의 시작과 같은 경우
            if diff == int(plans[i][2]):
                answer.append(plans[i][0])
            # 작업은 끝났는데 다음 작업까지 시간이 남은 경우
            elif diff > int(plans[i][2]):
                answer.append(plans[i][0])
                # 다음 작업 시작전까지 못다한 작업 진행
                if len(waits) > 0:
                    time = diff - int(plans[i][2])
                    complete = 0
                    for j in range(len(waits)):
                        # 못다한 작업을 남은 시간안에 해결 불가능한 경우
                        if time < waits[j][1]:
                            waits[j][1] -= time
                            break
                        # 못다한 작업 소요시간이 남은 시간과 일치
                        elif time == waits[j][1]:
                            complete += 1
                            answer.append(waits[j][0])
                            break
                        # 못다한 작업 하나 이상 할 수 있는 시간이 남을 경우
                        else:
                            complete += 1
                            time -= waits[j][1]
                            answer.append(waits[j][0])

                    if complete > 0:
                        waits = waits[complete:]

            # 작업 끝나기 전에 새로운 작업 시작해야하는 경우
            else:
                plans[i][2] = int(plans[i][2]) - diff
                waits.append([plans[i][0], plans[i][2], i])
                waits.sort(key=lambda x: -x[2])

        else:
            answer.append(plans[i][0])

    # 남은 작업들 시행
    for i in range(len(waits)):
        answer.append(waits[i][0])

    return answer