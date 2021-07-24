board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    new_board = list(map(list, zip(*board))) #zip을 이용하여 행,열을 switch
    for i in new_board:
        while i[0] == 0:
            del i[0] #0을 모두 지워준다

    result = []
    for i in range(len(moves)):
        index = moves[i] - 1
        if len(new_board[index]) != 0:
            result.append(new_board[index][0]) #뽑은 인형을 바구니에 차례대로 담음
            new_board[index][0] = 0
            for k in new_board:
                if 0 in k:
                    k.remove(0)
        else:
            continue



    #print(new_board)
    #print(result)
    len1 = len(result)
    str1 = map(str, result)
    str2 = ''.join(str1)

    for i in range(len(board)):
        target = 11 * (i+1)
        target2 = 0
        target = str(target)
        while target in str2:
            str2 = str2.replace(target, '')

    lis = list(str2)
    ans = list(map(int,lis))
    len2 = len(ans)
    #print(ans)
    answer = len1 - len2

    return answer

did = solution(board,moves)
print(did)




