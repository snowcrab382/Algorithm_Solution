def solution(n, arr1, arr2):
    bin_arr1 = []
    bin_arr2 = []
    result = []
    for i in arr1:
        if len(bin(i)[2:]) == n:
            bin_arr1.append(bin(i)[2:])
        else:
            bin_arr1.append('0'*(n-len(bin(i)[2:]))+bin(i)[2:])
    for j in arr2:
        if len(bin(j)[2:]) == n:
            bin_arr2.append(bin(j)[2:])
        else:
            bin_arr2.append('0'*(n-len(bin(j)[2:]))+bin(j)[2:])
    for x in range(n):
        temp = ''
        for y in range(n):
            if int(bin_arr1[x][y])|int(bin_arr2[x][y]):
                temp = temp + '#'
            else:
                temp = temp + ' '
        result.append(temp)

    return result