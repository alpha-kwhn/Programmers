board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]

#동적 프로그래밍을 이용한 점화식 계산이 효율성을 통과시켜줌
#구간을 돌면서 각 위치에서 만들 수 있는 정사각형의 최대 변 길이를 넣어주면 순회 1번에 답이나왔다..

def solution(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i != 0 and j != 0:
                if board[i][j] == 1:
                    target = min(board[i-1][j], board[i][j-1])
                    board[i][j] = min(target, board[i-1][j-1]) + 1
    lis = board[0]
    for i in range(1, len(board)):
        lis.extend(board[i])
    return max(lis) ** 2

did = solution(board)
print(did)