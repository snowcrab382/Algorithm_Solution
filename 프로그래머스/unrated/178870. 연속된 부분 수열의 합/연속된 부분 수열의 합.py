def solution(sequence, k):
    start, stop = 0, 0
    hap = sequence[0]
    cur_length = len(sequence)
    while stop < len(sequence):
        if hap == k:
            if stop - start < cur_length:
                result = [start, stop]
                cur_length = stop - start
            hap -= sequence[start]
            start += 1
        elif hap < k:
            stop += 1
            if stop < len(sequence):
                hap += sequence[stop]
        else:
            hap -= sequence[start]
            start += 1
    return result
            