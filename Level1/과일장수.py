# 1점 최하, k점 최상
# 1박스 M개 포장
# 상자 담긴 사과중 가장 낮은 점수가 P점 --> p * m이 가격이 된다
# 과일 장수가 가능한 많은 사과 팔았을 때, 얻을 수 있는 최대 이익을 계산하기

def solution(k, m, score):
    answer = 0
    lengths = len(score)

    if lengths % m != 0:
        score.sort(reverse=True)
        # [3 3 2 2 1 1 1]
        for i in range(0, (lengths // m)):
            answer += (score[(m * i) + (m - 1)] * m)

    else:
        score.sort()
        for i in range(0, (lengths // m)):
            answer += (score[(m * i)] * m)  # 0, 3

    return answer