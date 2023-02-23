def solution(s):
    answer = list(s.split())
    answer.sort(key = lambda x : int(x))
    return '{} {}'.format(answer[0],answer[-1])
    