citations = [1, 4]


def solution(citations):
    citations.sort()
    if max(citations) == 0:
        return 0
    else:
        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                return len(citations) - i


did = solution(citations)
print(did)





