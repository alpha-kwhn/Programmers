import itertools


def solution(babbling):
    answer = 0
    flag = 0
    sample = ["aya", "ye", "woo", "ma"]
    twice = ["ayaaya", "yeye", "woowoo", "mama"]

    lis = ["aya", "ye", "woo", "ma"]
    lis.extend(list(map(''.join, itertools.product(sample, repeat=4))))
    lis.extend(list(map(''.join, itertools.product(sample, repeat=3))))
    lis.extend(list(map(''.join, itertools.product(sample, repeat=2))))
    print(lis)

    for i in babbling:
        flag = 0
        if i in lis and (i * 2) not in lis:
            for j in twice:
                if j in i:
                    flag = 1

            if flag == 0:
                answer += 1

    return answer

print(solution(["aya", "yee", "u", "maa"]))