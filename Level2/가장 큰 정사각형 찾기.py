board = [[0,1,1,1],[1,1,1,1],[0,0,0,0],[0,0,1,0]]
board2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def solution(board):
    check = 0
    for i in board:
        for j in i:
            check += j
    if check == 0:
        return 0

    width = []
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            width.append(board[i][j])
            if board[i][j] == 1:
                count += 1
    target = []
    ans = []
    for i in range(1, int(count ** 0.5) + 1):
        target.append(i)
        ans.append(i * i)
    target.reverse()
    ans.reverse()

    total = []
    for i in target:
        all = []
        for u in range(0, (len(board) - i) + 1):
            for q in range(0, (len(board[0]) - i) + 1):
                result = 0
                for j in range(u, u+i):
                    for p in range(q, q+i):
                        if board[j][p] == 1:
                            result += board[j][p]
                        if result == i*i:
                            all.append(result)
                        elif board[j][p] == 0:
                            result = 0
                            break
        total.append(all)
    newer = total[0]
    for i in range(1, len(total)):
        newer.extend(total[i])
    print(newer)

    for i in range(len(ans)):
        if ans[i] not in newer:
            ans[i] = 0
        else:
            return ans[i]

did = solution(board)
print(did)
