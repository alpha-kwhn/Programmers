def solution(triangle):
    answer = []
    for i in range(len(triangle)-1):
        new = [0] * (i+2)
        for p in range(len(triangle[i])):
            a = triangle[i][p]
            for j in range(p, p+2):
                b = triangle[i+1][j]
                new[j] = max(new[j], a+b)
        triangle[i+1] = new
    return max(triangle[-1])