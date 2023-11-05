def solution(jobs):
    time = 0
    jobs = sorted(jobs, key=lambda x: x[1])
    num = len(jobs)
    total = 0

    while jobs:
        for idx in range(len(jobs)):
            # 현재시각 이전에 요청 발생한 작업 발견
            # 시간 갱신, 작업 목록에서 삭제,
            if jobs[idx][0] <= time:
                total += (jobs[idx][1] + (time - jobs[idx][0]))
                time += (jobs[idx][1] - 1)
                jobs.remove(jobs[idx])
                break
        time += 1
    return total // num