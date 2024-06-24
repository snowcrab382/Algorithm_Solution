def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x : (x[col-1], -x[0]))
    record_len = len(data[0])
    
    S_i = 0
    for i in range(row_begin-1, row_end):
        tmp = 0
        for j in data[i]:
            tmp += j % (i+1)
        S_i = S_i ^ tmp
    
    return S_i