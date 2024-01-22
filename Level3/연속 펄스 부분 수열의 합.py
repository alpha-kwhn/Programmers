def solution(sequence):
    if len(sequence) == 0:
        return 0
    elif len(sequence) == 1:
        return abs(sequence[0])
    else:
        lis_a = [sequence[0]]
        lis_b = [sequence[0] * -1]
        a = sequence[0]  # 홀양
        b = sequence[0] * -1  # 홀음
        for i in range(1, len(sequence)):
            if i % 2 == 1:
                target_a = (sequence[i] * -1)
                target_b = sequence[i]
                lis_a.append(max(lis_a[-1] + target_a, target_a))
                lis_b.append(max(lis_b[-1] + target_b, target_b))
            else:
                target_a = sequence[i]
                target_b = (sequence[i] * -1)
                lis_a.append(max(lis_a[-1] + target_a, target_a))
                lis_b.append(max(lis_b[-1] + target_b, target_b))
        return max(max(lis_a), max(lis_b))

