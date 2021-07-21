nums = [1, 2, 3, 4]
nums2 = [1, 2, 7, 6, 4]


def solutions(nums):
    prime_num = 0
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):

                sum = nums2[i]+nums2[j]+nums2[k]
                flag = 0

                for m in range(2, sum):
                    if sum % m == 0:
                        flag = 1
                        break

                if flag == 0:
                    prime_num += 1
    return prime_num

did = solutions(nums2)
print(did)
