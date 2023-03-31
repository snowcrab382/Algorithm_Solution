
count = 0
def solution(n):
    visited_1 = []
    visited_2 = []
    visited_3 = []

    def bt(r):
        global count
        if r == n:
            count += 1
        
        for i in range(n):
            if i not in visited_1 and i-r not in visited_2 and r+i not in visited_3:
                visited_1.append(i)
                visited_2.append(i-r)
                visited_3.append(r+i)
                bt(r+1)
                visited_1.pop()
                visited_2.pop()
                visited_3.pop()
    bt(0)
    return count
