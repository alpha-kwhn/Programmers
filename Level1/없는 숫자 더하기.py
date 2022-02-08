numbers = [1,2,3,4,6,7,8,0]

def solution(numbers):
    check = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in numbers:
        if i in check:
            check.remove(i)
    return sum(check)

print(solution(numbers))