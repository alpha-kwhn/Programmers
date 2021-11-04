rows = 3
columns = 3
queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]

def solution(rows, columns, queries):
    #행렬 만들기
    num = 1
    total = []
    for i in range(rows):
        target = []
        for j in range(columns):
            target.append(num)
            num += 1
        total.append(target)

    #쿼리 값 1씩 minus
    for i in queries:
        for k in range(len(i)):
            i[k] -= 1

    fin = []
    for i in queries:
        for j in range(len(i)):
            fin.append(total[j])



did = solution(rows, columns, queries)
print(did)