def solution(board):
    case = [[(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)]]

    x_count = 0
    o_count = 0
    comma_count = 0

    lis = []

    for i in board:
        x_count += i.count('X')
        o_count += i.count('O')
        comma_count += i.count('.')

    for row in case:
        target = ""
        for idx in row:
            target += board[idx[0]][idx[1]]
        if target == "OOO" or target == "XXX":
            lis.append(target)

    if len(lis) == 1:
        if lis[0] == "OOO":
            if o_count - x_count == 1:
                return 1
            else:
                return 0
        elif lis[0] == "XXX":
            if o_count - x_count == 0:
                return 1
            else:
                return 0
    elif len(lis) > 1:
        if len(list(set(lis))) == 1:
            if o_count - x_count == 1:
                return 1
            else:
                return 0
        else:
            return 0
    elif len(lis) == 0:
        if o_count + x_count == 9:
            if o_count == 5:
                return 1
            else:
                return 0
        elif 1 < o_count + x_count < 9:
            if o_count < x_count:
                return 0
            else:
                if o_count - x_count >= 2:
                    return 0
                else:
                    return 1
        elif o_count + x_count == 1:
            if o_count == 1:
                return 1
            else:
                return 0
        else:
            return 1