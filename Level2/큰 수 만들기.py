number = "4177252841"
k = 4

def solution(number, k):
    lis= []
    for i in number:
        while len(lis) > 0 and k > 0 and int(lis[-1]) < int(i):
            k -= 1
            lis.pop()
        lis.append(i)
    answer = ''.join(lis)
    return answer[:len(number)-k]


did = solution(number, k)
print(did)