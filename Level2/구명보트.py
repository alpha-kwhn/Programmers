people = [70, 50, 80]
limit = 100


def solution(people, limit):
    people.sort()
    count = 0
    answer = 0
    index = len(people) - 1

    while index >= count:
        tmp = people[index]
        index -= 1
        if people[count] + tmp <= limit:
            count += 1
            answer += 1
        else:
            answer += 1
    return answer






did = solution(people, limit)
print(did)