clothes = [["crowmask", "headgear"], ["bluesunglasses", "mask"],
           ["smoky_makeup", "headgear"], ["a", "mask"]]

def solution(clothes):
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


