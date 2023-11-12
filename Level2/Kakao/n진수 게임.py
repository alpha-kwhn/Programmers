def convert(num, n):
    target = []
    while num > 0:
        target.append(str(num % n))
        num //= n
    target.reverse()
    return target

def solution(n, t, m, p):
    result = ""
    dic = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    answer = ""
    i = 0
    count = 1
    
    while len(answer) < t:
        if i == 0:
            if p == 1:
                answer += '0'
                count += 1
                if count > m:
                    count = 1
            else:
                count += 1    
            i += 1
        else:
            tmp = convert(i, n)
            for idx in range(len(tmp)):
                if len(answer) < t:
                    if count == p:
                        if int(tmp[idx]) >= 10:
                            answer += dic[int(tmp[idx])]
                        else:
                            answer += tmp[idx]
                    count += 1
                    if count > m:
                        count = 1
                else:
                    break
            i += 1
    return answer
            
