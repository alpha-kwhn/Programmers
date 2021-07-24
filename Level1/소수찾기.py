n = 5

def solution(n):
    con = [True] * (n+1)

    #n의 최대 약수가 제곱근 이하이므로 i = sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if con[i] == True:
            for j in range(i+i, n+1, i):
                con[j] = False
    #j의 배수에 해당 하는 번지는 모두 False로 만들어준다
    answer = [i for i in range(2,n+1) if con[i] == True]
    return len(answer)
    #에라토스테네스의 체

did = solution(n)
print(did)
