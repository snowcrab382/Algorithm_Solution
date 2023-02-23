def solution(n, arr1, arr2):
    result = []
    for i in range(n):
        tmp = bin(arr1[i]|arr2[i])
        tmp = tmp[2:].zfill(n)
        tmp = tmp.replace('1','#').replace('0',' ')
        result.append(tmp)

    return result