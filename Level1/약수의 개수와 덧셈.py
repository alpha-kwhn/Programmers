left = 24
right = 27

def get_num(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

def solution(left, right):
    sum = 0

    for i in range(left, right+1):
        target = get_num(i)

        if target % 2 == 0:
            sum += i
        else:
            sum -= i

    return sum

did = solution(left, right)
print(did)




