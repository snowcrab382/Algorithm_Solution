def solution(a, b):
    answer = ''
    date = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    count = 0
    Day_of_week = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    for i in range(a):
        count += date[i]
    count += b
    answer = Day_of_week[count % 7]
    
    return answer