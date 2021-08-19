clothes = [["crowmask", "headgear"], ["bluesunglasses", "mask"],
           ["smoky_makeup", "headgear"], ["a", "mask"]]

def solution(clothes): #파스칼 삼각형 성질 이용
    # 2C1 + 2C0 = 3C1 (안고르는 경우 + 2개중 하나 고르는 경우) - 종류 당
    # 3C1 * 3C1 - 1(아무것도 안 고르는 경우)
    how = {}
    lis = []
    for i in clothes:
        if i[1] in lis:
            how[i[1]] += 1
        else:
            how[i[1]] = 1
            lis.append(i[1])
    mul = 1
    val = how.values()
    print(val)
    for i in val:
        mul *= i+1
    return mul - 1


did = solution(clothes)
print(did)


