month_list = {1:0, 2: 31, 3:59, 4:90, 5:120, 6:151,
     7:181, 8:212, 9:243, 10:273, 11:304, 12:334}
dayofweek_list = ['SUN','MON','TUE','WED','THU','FRI','SAT']
month,day = map(int,input().split())
day += month_list[month]
print(dayofweek_list[day%7])