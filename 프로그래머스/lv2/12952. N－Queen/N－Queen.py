
count = 0
def solution(n):
    visited_1 = [0] * 100
    visited_2 = [0] * 100
    visited_3 = [0] * 100

    def bt(r):
        global count
        if r == n:
            count += 1
        
        for i in range(n):
            if not visited_1[i] and not visited_2[i-r] and not visited_3[r+i]:
                visited_1[i] = 1
                visited_2[i-r] = 1
                visited_3[r+i] = 1
                bt(r+1)
                visited_1[i] = 0
                visited_2[i-r] = 0
                visited_3[r+i] = 0
    bt(0)
    return count
