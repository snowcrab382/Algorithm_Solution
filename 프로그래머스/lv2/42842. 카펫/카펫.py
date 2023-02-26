def solution(brown, yellow):
    for i in range(1,yellow+1):
        if yellow//i * i == yellow and (yellow//i+2)*(i+2) == brown+yellow:
            return [yellow//i+2,i+2]