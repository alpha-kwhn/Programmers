numbers = [2, 11]

def solution(numbers):
    answer = []
    for i in numbers:
        if i % 2 == 0:
            answer.append(i + 1)
        else:
            target = str(format(i, 'b'))
            if target[-2:] == '01':
                answer.append(i + 1)
            else:
                if '0' not in target:
                    answer.append(i + (2 ** (target.count('1') - 1)))
                else:
                    n = -1
                    while target[n] != '0':
                        n -= 1
                    index = abs(n) - 2
                    answer.append(i + (2 ** index))
    return answer

did = solution(numbers)
print(did)
