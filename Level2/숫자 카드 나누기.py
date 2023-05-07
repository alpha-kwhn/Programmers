def uclid(a, b):
    big = max(a, b)
    small = min(a, b)

    if small == 0:
        return big
    else:
        return uclid(small, big % small)


def gcdN(arr):
    gcd = arr[0]
    for i in range(1, len(arr)):
        gcd = uclid(gcd, arr[i])
    return gcd


def solution(arrayA, arrayB):
    target_a = gcdN(arrayA)
    target_b = gcdN(arrayB)

    status_a = 0
    status_b = 0

    for i in range(len(arrayA)):
        if arrayA[i] % target_b == 0:
            status_b = 1
        if arrayB[i] % target_a == 0:
            status_a = 1

    if status_b == 1 and status_a == 1:
        return 0
    else:
        return max(target_a, target_b)

