str1 = "aa1+aa2"
str2 = "AAAA12"

def solution(str1, str2):
    first = 0
    second = 1
    set_a = []
    set_b = []

    for i in range(len(str1)-1):
        answer = ''
        answer += str1[first]
        answer += str1[second]
        first += 1
        second += 1
        set_a.append(answer.lower())

    first = 0
    second = 1

    for i in range(len(str2)-1):
        answer = ''
        answer += str2[first]
        answer += str2[second]
        first += 1
        second += 1
        set_b.append(answer.lower())

    kyo = []
    hap = []

    for i in set_a:
        if i in set_b and i not in kyo:
            for m in range(min(set_a.count(i), set_b.count(i))):
                kyo.append(i)
        if i in set_b and i not in hap:
            for m in range(max(set_a.count(i), set_b.count(i))):
                hap.append(i)
        if i not in set_b and i not in hap:
            for m in range(max(set_a.count(i), set_b.count(i))):
                hap.append(i)

    for i in set_b:
        if i not in set_a and i not in hap:
            for m in range(max(set_a.count(i), set_b.count(i))):
                hap.append(i)

    real_kyo = []
    real_hap = []

    for i in kyo:
        if i.isalpha():
            real_kyo.append(i)
    for i in hap:
        if i.isalpha():
            real_hap.append(i)
    print(real_kyo)
    print(real_hap)

    if len(real_kyo) == 0 and len(real_hap) == 0:
        return 65536

    target = ((len(real_kyo) / len(real_hap)) * 65536)
    answer = int(target)
    return answer



did = solution(str1, str2)
print(did)