numbers = [3, 30, 34, 5, 9]

def solution(numbers):
    if max(numbers) == 0:
        return '0'
    numbers = list(map(str, numbers))
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 3
    numbers.sort()
    numbers.reverse()
    for i in range(len(numbers)):
        numbers[i] = numbers[i][:len(numbers[i]) // 3]
    return ''.join(numbers)

did = solution(numbers)
print(did)