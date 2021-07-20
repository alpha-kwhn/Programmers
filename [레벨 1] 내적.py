a = [4, 6, 1, 2]
b = [-1, -2, -3, 7]


def solution(a, b):
    size_a = len(a)
    sum = 0

    for i in range(size_a):
        sum += (a[i] * b[i])
    answer = sum
    return answer


ad = solution(a, b)
print(ad)
