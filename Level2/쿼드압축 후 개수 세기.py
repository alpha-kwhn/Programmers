arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]

#전체적인 과정을 재귀호출 방식을 통해 분해하면서 그때 그때 문제의 조건에 맞게 합쳐주는 작업을 하였다
def solution(arr):
    result = []
    def BFS(arr, middle):
        turn = []
        if middle != 1:
            for p in arr:
                for o in p:
                    turn.append(o)
            if 1 not in turn:
                result.append([0])
            elif 0 not in turn:
                result.append([1])
            else:
                check = []
                check2 = []
                check3 = []
                check4 = []
                for j in range(middle):
                    check.append(arr[j][:middle])
                    check2.append(arr[j+middle][:middle])
                    check3.append(arr[j][middle:])
                    check4.append(arr[j+middle][middle:])
                BFS(check, middle // 2)
                BFS(check2, middle // 2)
                BFS(check3, middle // 2)
                BFS(check4, middle // 2)
        else:
            for p in arr:
                for o in p:
                    turn.append(o)
            if 1 not in turn:
                result.append([0])
            elif 0 not in turn:
                result.append([1])
            else:
                result.append(turn)
    BFS(arr, len(arr) // 2)
    con = []
    for i in result:
        con += i
    return [con.count(0), con.count(1)]


did = solution(arr)
print(did)



