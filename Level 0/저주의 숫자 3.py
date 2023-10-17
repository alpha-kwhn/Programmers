def solution(n):
    # 가용 가능 숫자 모음
    able = []
    total = 0
    now = 1
    
    while total <= 100:
        if now % 3 != 0 and '3' not in str(now):
            able.append(now)
            total += 1
        now += 1 
    return able[n-1]
