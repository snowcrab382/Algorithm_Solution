import sys
sys.setrecursionlimit(10**6)

def solution(k, room_number):
    def check(num):
        if num not in reserved.keys():
            reserved[num] = num + 1
            return num
        
        empty = check(reserved[num])
        reserved[num] = empty + 1
        return empty
        
        
    answer = []    
    reserved = dict()
    for number in room_number:
        answer.append(check(number))
    
    return answer