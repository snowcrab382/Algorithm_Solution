import math

def solution(arr):
    i = 1
    while True:
        i += 1
        pos = True
        for x in arr:
            if i % x != 0:
                pos = False
                break
        if pos:
            return i
    print(i)