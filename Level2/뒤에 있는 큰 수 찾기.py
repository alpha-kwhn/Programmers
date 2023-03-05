def solution(numbers):
    # 0. 정답 배열 -> -1로 전부 일단 초기화
    answer = [-1] * len(numbers)
    # 1. 자신보다 큰 수가 나올 때까지 대기시킬 값을 담는 stack
    stack = []
    # 2. 배열 순회
    for i in range(len(numbers)):
        # 2.1 맨 첫 번째 값에서는 인덱스만 저장
        if i == 0:
            stack.append(i)
        # 2.2 첫 번째 값이 아니라면
        else:
            # 2.2.1 Stack이 빌 때까지 top 값을 numbers[i]랑 계속 비교
            while stack:
                # 2.2.2 Stack의 top 값이 numbers[i] 보다 작을 경우
                if numbers[stack[-1]] < numbers[i]:
                    # pop으로 삭제 & pop한 값의 해당 인덱스의 answer 값 변경
                    answer[stack[-1]] = numbers[i]
                    stack.pop(-1)
                # 2.2.3 Stack의 top 값이 numbers[i] 보다 큰 경우
                else:
                    # break
                    break
            # 현재 비교 인덱스 값 stack에 추가
            stack.append(i)
    return answer