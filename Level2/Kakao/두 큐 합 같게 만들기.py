# 하나의 큐를 골라 원소 추출, 추출된 원소를 다른 큐에 집어넣기
# 이 작업을 통해 각 큐의 원소 합이 같도록 만듬
# 이 때, 필요한 작업의 최소 횟수 구하기 (1pop, 1insert = 1 시퀀스)
# FIFO 구조
from collections import deque


def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    max1 = max(queue1)
    max2 = max(queue2)
    lengths = len(queue1) * 2

    # 합이 홀수라면 합 같게 만들기 불가능
    if (sum1 + sum2) % 2 == 1:
        return -1
    else:
        if sum1 > sum2 and ((max1 > (sum1 - max1) + sum2) or (max2 > (sum2 - max2) + sum1)):
            return -1
        elif sum1 < sum2 and ((max2 > (sum2 - max2) + sum1) or (max1 > (sum1 - max1) + sum2)):
            return -1

        flag_1 = 0
        flag_2 = 0

        # 1바퀴 다 돌때까지 계속 진행
        while flag_1 < lengths and flag_2 < lengths:
            if sum1 > sum2:
                num = queue1.popleft()
                sum1 -= num
                queue2.append(num)
                sum2 += num
                answer += 1
                flag_1 += 1
            elif sum1 < sum2:
                num = queue2.popleft()
                sum2 -= num
                queue1.append(num)
                sum1 += num
                answer += 1
                flag_2 += 1
            else:
                return answer

        return -1