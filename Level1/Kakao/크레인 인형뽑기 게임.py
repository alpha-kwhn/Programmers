board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    new_board = list(map(list, zip(*board)))  # zip을 이용하여 행,열을 switch
    for i in new_board:
        if i.count(0) != len(board): #빈 열이 없는 경우
            while i[0] == 0:
                del i[0]  # 0을 모두 지워준다
        elif i.count(0) == len(board): #빈 열이 존재하는 경우
            i.clear()
            i.append(0) #0하나만 남겨준다(구분값)

    for i in new_board: #이중 리스트 중 내부 리스트를 전부 reverse 해준다(pop()이용을 위함)
        i.reverse()

    result = []
    count = 0
    index = moves[0] - 1
    if 0 not in new_board[index]: #최초에 크레인이 인형이 존재하는 열에 들어갔을 때만 인형 저장
        trash = new_board[index].pop()
        result.append(trash)
        count += 1

    for i in range(1, len(moves)): #인형뽑기 과정
        index = moves[i] - 1
        if 0 not in new_board[index] and len(new_board[index]) != 0:
            #인형상자에 빈열이 존재하지 않을 시에 크레인의 동작
            trash = new_board[index].pop()
            if len(result) == 0:
                result.append(trash)
            else:
                if result[-1] == trash:
                    trash2 = result.pop()
                else:
                    result.append(trash)
            count += 1
        else: #인형상자에 빈 열이 존재하는 경우에는 크레인은 동작을 생략한다
            continue

    answer = count - len(result)
    return answer

did = solution(board, moves)
print(did)
