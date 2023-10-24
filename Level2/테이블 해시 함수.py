def solution(data, col, row_begin, row_end):
    data = sorted(data, key=lambda x: (x[col-1], -x[0]))
    target = []
    
    for idx in range(row_begin, row_end + 1):
        num = 0
        for item in range(len(data[0])):
            num += (data[idx-1][item] % idx)
        target.append(num)
        
        if len(target) == 2:
            result = target[0] ^ target[1]
            target = [result]
    return target[0]
