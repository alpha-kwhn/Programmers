num = 3


def solution(num):
    ans = ["Odd", "Even"]
    if num % 2 == 0:
        return ans[1]
    else:
        return ans[0]

did = solution(num)
print(did)