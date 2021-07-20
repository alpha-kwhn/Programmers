
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):

    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p

    return p[-1]



did = solution(participant, completion)
print(did)
