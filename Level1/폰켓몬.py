nums = [3, 1, 2, 3]
nums2 = [3,3,3,2,2,4]
nums3 = [3,3,3,2,2,2]


def solution(nums):
    pick = len(nums) // 2
    set_nums = set(nums)
    answer = 0

    if pick < len(set_nums):
        answer = pick
        return answer
    else:
        answer = len(set_nums)
        return answer

did = solution(nums)
print(did)
did1 = solution(nums2)
print(did1)
did2 = solution(nums3)
print(did2)