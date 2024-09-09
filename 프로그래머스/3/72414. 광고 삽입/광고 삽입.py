def time_to_second(time):
    h, m, s = map(int, time.split(":"))
    return h * 3600 + m * 60 + s

def second_to_time(sec):
    h, m, s = sec // 3600, sec % 3600 // 60, sec % 60
    return f'{h:02}:{m:02}:{s:02}'

def solution(play_time, adv_time, logs):
    play = time_to_second(play_time)
    adv = time_to_second(adv_time)
    
    viewers = [0 for _ in range(100 * 60 * 60 + 1)]

    for log in logs:
        start, end = map(time_to_second, log.split('-'))
        viewers[start] += 1
        viewers[end] -= 1
        
    p = 0
    viewers[1] += 2 * viewers[0]
    for i in range(2, len(viewers)):
        viewers[i] += 2 * viewers[i-1] -viewers[i-2]         
    
    mx = viewers[adv]
    answer = 0
    
    for t in range(1, play-adv+1):
        view = viewers[t + adv-1] - viewers[t - 1]
        if view > mx:
            mx = view
            answer = t
        
    return second_to_time(answer)